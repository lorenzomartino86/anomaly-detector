import unittest
from unittest import TestCase

from unittest.mock import patch, call

from src.adapter.repository.SFTPFileRepository import SFTPFileRepository
from src.adapter.repository.sftp.RemoteFile import RemoteFile


class TestSFTPFileRepository(TestCase):

    def test_retrieve(self):

        with patch('paramiko.SSHClient') as sftp_mock:
            hostname = 'host.test'
            username = 'user'
            password = 'password'
            remote_file = RemoteFile('/home/remote/file.txt')
            local_file = RemoteFile('/home/local/file.txt')
            repository = SFTPFileRepository(hostname=hostname,
                                            username=username,
                                            password=password,
                                            remote_file=remote_file,
                                            local_file=local_file)

            repository.get()

if __name__ == '__main__':
    unittest.main()
