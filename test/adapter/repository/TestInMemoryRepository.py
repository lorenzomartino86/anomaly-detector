import unittest

import os

from src.adapter.repository.InMemoryRepository import InMemoryRepository

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestInMemoryRepository(unittest.TestCase):

    def setUp(self):
        self.data = list()
        self.data.append(1)
        self.data.append(2)
        self.data.append(3)
        self.repository = InMemoryRepository(data=self.data)

    def test_get_from_repository(self):
        records = self.repository.get()
        self.assertEqual(len(records), 3, "it should retrieve three numbers")

if __name__ == '__main__':
    unittest.main()
