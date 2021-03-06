import unittest

from src.adapter.notification.InMemoryBroker import InMemoryBroker
from src.adapter.repository.FileRepository import FileRepository
from src.domain.usecase.ClusterClassifier import ClusterClassifier
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestClusterClassifier(unittest.TestCase):

    def setUp(self):
        train_repository = FileRepository(file=open(ROOT_DIR + '/../../resources/train.txt'))
        test_repository = FileRepository(file=open(ROOT_DIR + '/../../resources/test.txt'))

        self.detector = ClusterClassifier(train_repository=train_repository,
                                          test_repository=test_repository,
                                          notifier=InMemoryBroker(),
                                          train_persister=None,
                                          outlier_persister=None)

    def test_one_cluster(self):
        clusters = self.detector.detect_outliers()

        self.assertEqual(len(clusters), 2, "2 new clusters should be detected")

if __name__ == '__main__':
    unittest.main()
