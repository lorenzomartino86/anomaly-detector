import unittest

from src.adapter.repository.FileRepository import FileRepository
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestFileRepository(unittest.TestCase):

    def setUp(self):
        self.repository = FileRepository(file=open(ROOT_DIR + '/../../resources/train.txt'))

    def test_get_from_repository(self):
        records = self.repository.get()
        self.assertEqual(len(records), 3, "it should retrieve three records")

if __name__ == '__main__':
    unittest.main()
