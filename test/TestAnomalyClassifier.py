import unittest

from AnomalyClassifier import LogClassifier
from src.adapter.persister.FilePersister import FilePersister
from src.adapter.repository.FileRepository import FileRepository
from src.adapter.repository.parser import FileParser


class TestAnomalyClassifier(unittest.TestCase):

    def test_(self):
        classifier = LogClassifier()
        classifier.add_repository(FileRepository(train_path="resources/train.txt",
                                             test_path="resources/test.txt"))
        classifier.add_persister(FilePersister(base_path="resources"))
        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 2, "it should retrieve ### new clusters")

if __name__ == '__main__':
    unittest.main()
