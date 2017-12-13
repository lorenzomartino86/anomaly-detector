import unittest

from src.adapter.repository.FileRepository import FileRepository
from src.domain.usecase.AnomalyFromLog import AnomalyFromLog

class TestAnomalyFromLog(unittest.TestCase):

    def setUp(self):
        repository = FileRepository(train_file=open('../../resources/train.txt'),
                                    test_file=open('../../resources/test.txt'))
        self.logDetector = AnomalyFromLog(repository=repository, notifier=None, persister=None)

    def test_one_cluster(self):
        clusters = self.logDetector.detect_anomaly()
        self.assertEqual(len(clusters), 2, "2 new clusters should be detected")

if __name__ == '__main__':
    unittest.main()
