import unittest
import os

import datetime

from AnomalyClassifier import LogClassifier
from src.adapter.notification.InMemoryBroker import InMemoryBroker
from src.adapter.persister.FilePersister import FilePersister
from src.adapter.repository.FileRepository import FileRepository
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestAnomalyClassifier(unittest.TestCase):

    def test_log_classifier(self):
        classifier = LogClassifier()

        classifier.add_train_repository(FileRepository(file=open(ROOT_DIR + '/resources/train.txt')))
        classifier.add_test_repository(FileRepository(file=open(ROOT_DIR + '/resources/test.txt')))

        persister = FilePersister(base_path=ROOT_DIR + '/resources')
        today = datetime.datetime.today()
        cluster_persisted_filename = "clusters_" + today.strftime('%Y-%m-%d') + ".obj"
        classifier.add_persister(persister)

        notifier = InMemoryBroker()
        classifier.add_notifier(notifier=notifier)

        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 2,
                         "it should retrieve 2 new clusters")

        self.assertEqual(len(notifier.queue.get()), 2,
                         "it should retrieve 2 new clusters notified to Broker")

        self.assertEqual(len(persister.get(cluster_persisted_filename)), 2,
                         "it should retrieve 2 new persisted clusters")

        persister.remove(cluster_persisted_filename)


    def test_complex_classification(self):
        classifier = LogClassifier()

        classifier.add_train_repository(FileRepository(file=open(ROOT_DIR + '/resources/complex_train.txt')))
        classifier.add_test_repository(FileRepository(file=open(ROOT_DIR + '/resources/complex_test.txt')))

        persister = FilePersister(base_path=ROOT_DIR + '/resources')
        today = datetime.datetime.today()
        cluster_persisted_filename = "clusters_" + today.strftime('%Y-%m-%d') + ".obj"
        classifier.add_persister(persister)

        notifier = InMemoryBroker()
        classifier.add_notifier(notifier=notifier)

        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 3,
                         "it should retrieve 3 new clusters")

        self.assertEqual(len(notifier.queue.get()), 3,
                         "it should retrieve 3 new clusters notified to Broker")

        self.assertEqual(len(persister.get(cluster_persisted_filename)), 3,
                         "it should retrieve 3 new persisted clusters")

        persister.remove(cluster_persisted_filename)

if __name__ == '__main__':
    unittest.main()
