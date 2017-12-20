import unittest

from src.adapter.notification.InMemoryBroker import InMemoryBroker
from src.adapter.repository.FileRepository import FileRepository
from src.domain.usecase.AnomalyFromLog import AnomalyFromLog
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAnomalyFromLog(unittest.TestCase):

    def setUp(self):
        train_repository = FileRepository(file=open(ROOT_DIR + '/../../resources/train.txt'))
        test_repository = FileRepository(file=open(ROOT_DIR + '/../../resources/test.txt'))

        self.logDetector = AnomalyFromLog(train_repository=train_repository,
                                          test_repository=test_repository,
                                          notifier=InMemoryBroker(),
                                          train_persister=None,
                                          test_persister=None)

    def test_one_cluster(self):
        clusters = self.logDetector.detect_anomaly()

        self.assertEqual(len(clusters), 2, "2 new clusters should be detected")

if __name__ == '__main__':
    unittest.main()
