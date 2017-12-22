import unittest
import os

from datetime import datetime, timedelta

from AnomalyClassifier import LogClassifier
from src.adapter.notification.InMemoryBroker import InMemoryBroker
from src.adapter.persister.FilePersister import FilePersister
from src.adapter.repository.FileRepository import FileRepository
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestAnomalyClassifier(unittest.TestCase):

    def test_log_classifier(self):
        outlier_persister, train_persister = self.get_persisters()

        classifier = LogClassifier()

        classifier.add_train_repository(FileRepository(file=open(ROOT_DIR + '/../resources/train.txt')))
        classifier.add_test_repository(FileRepository(file=open(ROOT_DIR + '/../resources/test.txt')))

        classifier.add_outlier_persister(outlier_persister)
        classifier.add_train_persister(train_persister)

        notifier = InMemoryBroker()
        classifier.add_notifier(notifier=notifier)

        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 2,
                         "it should retrieve 2 new clusters")

        self.assertEqual(len(notifier.queue.get()), 2,
                         "it should retrieve 2 new clusters notified to Broker")

        self.assertEqual(len(outlier_persister.get()), 2,
                         "it should retrieve 2 new persisted clusters")

        outlier_persister.remove()

    def test_complex_classification(self):

        outlier_persister, train_persister = self.get_persisters()

        classifier = LogClassifier()

        classifier.add_train_repository(FileRepository(file=open(ROOT_DIR + '/../resources/complex_train.txt')))
        classifier.add_test_repository(FileRepository(file=open(ROOT_DIR + '/../resources/complex_test.txt')))

        classifier.add_train_persister(train_persister)
        classifier.add_outlier_persister(outlier_persister)

        notifier = InMemoryBroker()
        classifier.add_notifier(notifier=notifier)

        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 3,
                         "it should retrieve 3 new clusters")

        self.assertEqual(len(notifier.queue.get()), 3,
                         "it should retrieve 3 new clusters notified to Broker")

        self.assertEqual(len(outlier_persister.get()), 3,
                         "it should retrieve 3 new persisted clusters")

        outlier_persister.remove()


    def test_log_classifier_with_persisted_train_clusters(self):

        outlier_persister, train_persister = self.get_persisters()
        train_persister.save(object=None)

        classifier = LogClassifier()

        classifier.add_train_repository(FileRepository(file=open(ROOT_DIR + '/../resources/train.txt')))
        classifier.add_test_repository(FileRepository(file=open(ROOT_DIR + '/../resources/test.txt')))

        classifier.add_train_persister(train_persister)
        classifier.add_outlier_persister(outlier_persister)

        notifier = InMemoryBroker()
        classifier.add_notifier(notifier=notifier)

        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 2,
                         "it should retrieve 2 new clusters")

        self.assertEqual(len(notifier.queue.get()), 2,
                         "it should retrieve 2 new clusters notified to Broker")

        self.assertEqual(len(outlier_persister.get()), 2,
                         "it should retrieve 2 new persisted clusters")

        outlier_persister.remove()

    def get_persisters(self):
        today = datetime.today()
        yesterday = datetime.today() - timedelta(days=1)
        outlier_persiter_file = "clusters_" + today.strftime('%Y-%m-%d') + ".obj"
        train_persister_file = "clusters_" + yesterday.strftime('%Y-%m-%d') + ".obj"
        outlier_persister = FilePersister(file=ROOT_DIR + '/../resources/' + outlier_persiter_file)
        train_persister = FilePersister(file=ROOT_DIR + '/../resources/' + train_persister_file)
        return outlier_persister, train_persister

if __name__ == '__main__':
    unittest.main()
