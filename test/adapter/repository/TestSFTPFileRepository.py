import unittest
from unittest import TestCase

from unittest.mock import patch, call

from src.adapter.repository.SFTPFileRepository import SFTPFileRepository


class TestSFTPFileRepository(TestCase):

    def test_retrieve(self):

        with patch('') as sftp_mock:
            hostname = 'host.test'
            username = 'user'
            password = 'password'
            remote_file = '/home/remote/file.txt'
            local_file = '/home/local/file.txt'
            repository = SFTPFileRepository(hostname=hostname,
                                            username=username,
                                            password=password,
                                            remote_file=remote_file,
                                            local_file=local_file)

            repository.get()

if __name__ == '__main__':
    unittest.main()
