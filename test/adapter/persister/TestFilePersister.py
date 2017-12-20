import unittest

from src.adapter.persister.FilePersister import FilePersister
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestFilePersister(unittest.TestCase):

    def setUp(self):
        self.persister = FilePersister(base_path=ROOT_DIR + '/../../resources')

    def test_load_new_persister(self):
        object = list()
        object.append(1)
        object.append(2)
        self.persister.save("test_persister.obj", object)
        self.assertEqual(self.persister.get("test_persister.obj"), [1,2], "it should retrieve a list object [1,2]")

    def test_remove_persister(self):
        object = list()
        object.append(1)
        object.append(2)
        self.persister.save("test_persister.obj", object)
        self.persister.remove("test_persister.obj")

        with self.assertRaises(ValueError):
            self.persister.get("test_persister.obj")

if __name__ == '__main__':
    unittest.main()
