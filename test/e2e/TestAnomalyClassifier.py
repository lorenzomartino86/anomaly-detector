import unittest
import os

from AnomalyClassifier import LogClassifier
from src.adapter.persister.FilePersister import FilePersister
from src.adapter.repository.FileRepository import FileRepository
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestAnomalyClassifier(unittest.TestCase):

    def test_log_classifier(self):
        classifier = LogClassifier()

        classifier.add_repository(FileRepository(train_file=open(ROOT_DIR + '/resources/test.txt'),
                                             test_file=open(ROOT_DIR + '/resources/test.txt')))
        classifier.add_persister(FilePersister(base_path=ROOT_DIR + 'resources'))
        classifier = classifier.compile()

        new_clusters = classifier.detect_anomaly()

        self.assertEqual(len(new_clusters), 1, "it should retrieve 1 new cluster")

if __name__ == '__main__':
    unittest.main()
