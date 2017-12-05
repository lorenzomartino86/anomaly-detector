import unittest

from adapter.repository.FileRepository import FileRepository
from domain.cosine_similarity.ClusterGenerator import ClusterGenerator
from domain.cosine_similarity.RawInput import RawInput
from domain.cosine_similarity.TextProcessor import TextProcessor


class TestFileRepository(unittest.TestCase):

    def setUp(self):
        self.repository = FileRepository(train_path='../../resources/train.txt',
                                         test_path='../../resources/test.txt')

    def test_get_from_repository(self):
        train_records, test_records = self.repository.get()
        self.assertEqual(len(train_records), 3, "it should retrieve three train records")
        self.assertEqual(len(test_records), 2, "it should retrieve two test records")

if __name__ == '__main__':
    unittest.main()
