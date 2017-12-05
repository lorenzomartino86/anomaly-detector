import unittest

from adapter.repository.FileRepository import FileRepository
from domain.cosine_similarity.ClusterGenerator import ClusterGenerator
from domain.cosine_similarity.RawInput import RawInput
from domain.cosine_similarity.TextProcessor import TextProcessor


class TestFileRepository(unittest.TestCase):

    def setUp(self):
        self.repository = FileRepository(path='../../resources/train.txt')

    def test_get_from_repository(self):
        records = self.repository.get()
        self.assertEqual(len(records), 3, "it should retrieve three records")

if __name__ == '__main__':
    unittest.main()
