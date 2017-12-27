from os.path import expanduser

import paramiko as paramiko

from src.adapter.repository.parser.SimpleParser import SimpleParser
from src.decorator.logging import exception

class SFTPFileRepository(object):
    def __init__(self, hostname, port, username, password, remote_file, local_file, parser=SimpleParser()):
        self.hostname = hostname
        self.port = port
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


class SSHClient(object):
    def __init__(self, ssh_key_file, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(hostname=hostname, username=username, compress=True,
                            key_filename=ssh_key_file, password=password)

    def copy(self, from_file, to_file):
        stdin, stdout, stderr = self.client.exec_command('cp {0} {1}'.format(from_file, to_file))
        status = stdout.channel.recv_exit_status()  # Blocking until copy is done
        if status == 0:
            print('File {0} copied to /tmp'.format(from_file))
        else:
            print('Fail copy {0} to /tmp'.format(from_file))

    def find(self, remote_file):
        stdin, stdout, stderr = self.client.exec_command(
            'cd /{0}; find . -name app*'.format(remote_file.get_path()))
        stdout.channel.recv_exit_status()
        files = stdout.readlines()
        remote_files = [RemoteFile(file) for file in files]
        return remote_files

    def remove(self, file):
        stdin, stdout, stderr = self.client.exec_command('rm {0}'.format(file))
        status = stdout.channel.recv_exit_status()  # Blocking until copy is done
        if status == 0:
            print('File {0} removed'.format(file))
        else:
            print('Fail removing {0}'.format(file))

    def sftp_session(self, remote_file, local_file):
        session = self.client.open_sftp()
        try:
            session.get(remote_file, local_file)
        finally:
            session.close()

    def disconnect(self):
        self.client.disconnect()


class RemoteFile(object):
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return self.path.split('-', 3)[3].replace('/', '-').strip()

    def get_path(self):
        return self.path
