import unittest

from src.adapter.repository.FileRepository import FileRepository

class TestFileRepository(unittest.TestCase):

    def setUp(self):
        self.repository = FileRepository(train_file=open('../../resources/train.txt'),
                                         test_file=open('../../resources/test.txt'))

    def test_get_from_repository(self):
        train_records, test_records = self.repository.get()
        self.assertEqual(len(train_records), 3, "it should retrieve three train records")
        self.assertEqual(len(test_records), 2, "it should retrieve two test records")

if __name__ == '__main__':
    unittest.main()
