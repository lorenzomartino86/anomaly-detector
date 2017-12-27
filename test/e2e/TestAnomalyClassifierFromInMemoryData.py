import unittest
import os

from datetime import datetime, timedelta

from AnomalyClassifier import LogClassifier
from src.adapter.notification.InMemoryBroker import InMemoryBroker
from src.adapter.persister.FilePersister import FilePersister
from src.adapter.repository.InMemoryRepository import InMemoryRepository
from src.domain.pipeline.ClusterPipeline import ClusterPipeline

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAnomalyClassifierFromInMemoryData(unittest.TestCase):
    def test_log_classifier(self):
        test_data, train_data = self.get_train_and_test_data()

        classifier = LogClassifier(train_repository=InMemoryRepository(data=train_data),
                                   test_repository=InMemoryRepository(data=test_data),
                                   notifier=InMemoryBroker())

        classifier = classifier.compile()

        outliers = classifier.detect_anomaly()

        self.assertEqual(len(outliers), 3,
                         "it should retrieve 3 outliers")

        self.assertEqual(len(classifier.notifier.queue.get()), 3,
                         "it should retrieve 3 outliers notified to Broker")

    def test_cluster_classifier(self):
        train_data = list()
        train_data.append("Hello world")
        train_data.append("Uncle Bob")

        test_data = list()
        test_data.append("It's an outlier")
        test_data.append("Hello world")

        classifier = LogClassifier(train_repository=InMemoryRepository(data=train_data),
                                   test_repository=InMemoryRepository(data=test_data),
                                   notifier=InMemoryBroker(),
                                   pipeline=ClusterPipeline())
        classifier = classifier.compile()

        outliers = classifier.detect_anomaly()

        for outlier in outliers:
            print (outlier.records)

        self.assertEqual(len(outliers), 1,
                         "it should retrieve 1 outliers")

        self.assertEqual(len(classifier.notifier.queue.get()), 1,
                         "it should retrieve 1 outliers notified to Broker")


    def test_log_classifier_with_persisted_train_clusters(self):
        outlier_persister, train_persister = self.get_persisters()
        test_data, train_data = self.get_train_and_test_data()
        train_persister.save(object=None)

        classifier = LogClassifier(train_repository=InMemoryRepository(data=train_data),
                                   test_repository=InMemoryRepository(data=test_data),
                                   notifier=InMemoryBroker())
        classifier.add_outlier_persister(outlier_persister)
        classifier = classifier.compile()

        outliers = classifier.detect_anomaly()

        self.assertEqual(len(outliers), 3,
                         "it should retrieve 3 outliers")

        self.assertEqual(len(classifier.notifier.queue.get()), 3,
                         "it should retrieve 3 outliers notified to Broker")

        self.assertEqual(len(classifier.outlier_persister.get()), 3,
                         "it should retrieve 3 outliers clusters")

        classifier.outlier_persister.remove()

    @staticmethod
    def get_persisters():
        today = datetime.today()
        yesterday = datetime.today() - timedelta(days=1)
        outlier_persiter_file = "clusters_" + today.strftime('%Y-%m-%d') + ".obj"
        train_persister_file = "clusters_" + yesterday.strftime('%Y-%m-%d') + ".obj"
        outlier_persister = FilePersister(file=ROOT_DIR + '/../resources/' + outlier_persiter_file)
        train_persister = FilePersister(file=ROOT_DIR + '/../resources/' + train_persister_file)
        return outlier_persister, train_persister

    @staticmethod
    def get_train_and_test_data():
        train_data = list()
        train_data.append("CIAO CIAO CIAO")
        train_data.append("BELLA BELLA BELLA")
        train_data.append("CIAO CIAO BELLA CIAO")
        test_data = list()
        test_data.append("NEW LOG")
        test_data.append("CIAO CIAO CIAO")
        test_data.append("BAD NEWS")
        test_data.append("MERRY CHRISTMAS")
        return test_data, train_data


if __name__ == '__main__':
    unittest.main()
