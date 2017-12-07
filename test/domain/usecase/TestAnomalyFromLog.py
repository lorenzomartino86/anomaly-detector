import unittest

from src.adapter.repository.FileRepository import FileRepository
from src.domain.usecase import AnomalyFromLog


class TestAnomalyFromLog(unittest.TestCase):

    def setUp(self):
        repository = FileRepository(train_path='../../resources/train.txt',
                                    test_path='../../resources/test.txt')
        self.logDetector = AnomalyFromLog(repository=repository)

    def test_one_cluster(self):
        clusters = self.logDetector.detect_anomaly()
        self.assertEqual(len(clusters), 2, "2 new clusters should be detected")

if __name__ == '__main__':
    unittest.main()
