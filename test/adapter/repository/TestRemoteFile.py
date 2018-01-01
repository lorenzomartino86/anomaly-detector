import unittest
from unittest import TestCase

from src.adapter.repository.sftp.RemoteFile import RemoteFile


class TestRemoteFile(TestCase):
    def test_get_name(self):
        file = RemoteFile('/home/remote/file.txt')
        self.assertEqual(file.get_name(), 'file.txt')

    def test_get_extension(self):
        file = RemoteFile('/home/remote/file.txt')
        self.assertEqual(file.get_extension(), 'txt')

    def test_get_path(self):
        file = RemoteFile('/home/remote/file.txt')
        self.assertEqual(file.get_path(), '/home/remote/file.txt')

if __name__ == '__main__':
    unittest.main()
