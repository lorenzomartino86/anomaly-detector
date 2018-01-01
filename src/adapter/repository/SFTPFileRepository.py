from os.path import expanduser

from src.adapter.repository.parser.SimpleParser import SimpleParser
from src.adapter.repository.sftp.SSHClient import SSHClient
from src.decorator.logging import exception


class SFTPFileRepository(object):
    def __init__(self, hostname, username, password, remote_file, local_file, parser=SimpleParser()):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.remote_file = remote_file
        self.local_file = local_file
        self.parser = parser
        home = expanduser('~')
        ssh_key_file = home + "/.ssh/id_rsa"
        self.client = SSHClient(ssh_key_file=ssh_key_file, hostname=self.hostname,
                                username=self.username, password=self.password)

    @exception
    def get(self):
        self.transport(remote_file=self.remote_file,
                       local_file=self.local_file,
                       temp_file="/tmp/" + self.local_file.get_name())
        records = self.parser.parse(self.local_file)
        self.local_file.close()
        return records

    @exception
    def transport(self, remote_file, temp_file, local_file):
        self.client.copy(from_file=remote_file, to_file=temp_file)
        self.client.sftp_session(remote_file=temp_file, local_file=local_file)
        self.client.remove(file=temp_file)
