import unittest

from adapter.repository.FileRepository import FileRepository
from domain.usecase.LogDetector import LogDetector


class TestLogDetector(unittest.TestCase):

    def setUp(self):
        repository = FileRepository(train_path='../../resources/train.txt',
                                    test_path='../../resources/test.txt')
        self.logDetector = LogDetector(repository=repository)

    def test_one_cluster(self):
        clusters = self.logDetector.detect_anomaly()
        self.assertEqual(len(clusters), 2, "2 new clusters should be detected")

if __name__ == '__main__':
    unittest.main()
