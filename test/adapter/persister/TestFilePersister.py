import unittest

from src.adapter.persister.FilePersister import FilePersister
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestFilePersister(unittest.TestCase):

    def setUp(self):
        self.persister = FilePersister(file=ROOT_DIR + '/../../resources/test_persister.obj')

    def test_load_new_persister(self):
        object = list()
        object.append(1)
        object.append(2)
        self.persister.save( object)
        self.assertEqual(self.persister.get(), [1,2], "it should retrieve a list object [1,2]")

    def test_remove_persister(self):
        object = list()
        object.append(1)
        object.append(2)
        self.persister.save(object)
        self.persister.remove()

        with self.assertRaises(ValueError):
            self.persister.get()

if __name__ == '__main__':
    unittest.main()
