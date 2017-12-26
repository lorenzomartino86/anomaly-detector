import os
from os.path import expanduser

import paramiko as paramiko

from src.adapter.repository.parser.SimpleParser import SimpleParser
from src.decorator.logging import exception


class RemoteFileRepository(object):
    def __init__(self, hostname, port, username, password, file, parser=SimpleParser()):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.file = file
        self.parser = parser
        home = expanduser('~')
        ssh_key_file = home + "/.ssh/id_rsa"
        self.client = SSHClient(ssh_key_file=ssh_key_file, hostname=self.hostname,
                                username=self.username, password=self.password)

    def get(self):
        records = self.parser.parse(self.file)
        self.file.close()
        self.disconnect()
        return records

    @exception
    def disconnect(self):
        self.client.diconnect()


class SSHClient(object):
    def __init__(self, ssh_key_file, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(hostname=hostname, username=username, compress=True,
                            key_filename=ssh_key_file, password=password)

    def command(self, command):
        return self.client.exec_command(command=command)

    def sftp_session(self, remote_path, local_path):
        session = self.client.open_sftp()
        try:
            session.get(remote_path, local_path)
        finally:
            session.close()

    def disconnect(self):
        self.client.disconnect()


class FileRetriever(object):
    def __init__(self, client, remote_path, local_path, appname):
        self.client = client
        self.remote_path = remote_path
        self.local_path = local_path
        self.appname = appname

    def find(self, date):
        try:
            stdin, stdout, stderr = self.client.exec_command(
                'cd /{0}/{1}; find . -name app*'.format(self.remote_path, self.appname))
            stdout.channel.recv_exit_status()
            files = stdout.readlines()
            remote_files = [RemoteFile(file) for file in files]
            return remote_files
        except Exception as e:
            raise e
        finally:
            self.client.disconnect()

    def transport(self, file):
        tmp_file = '/tmp/' + file.get_name()
        stdin, stdout, stderr = self.client.exec_command('cp {0} {1}'.format(
            self.fullpath(file, self.remote_path, self.appname), tmp_file))
        status = stdout.channel.recv_exit_status()  # Blocking until copy is done
        if status == 0:
            print('File {0} copied to /tmp'.format(file.get_name()))
        else:
            print('Fail copy {0} to /tmp'.format(file.get_name()))
        self.client.sftp_session(tmp_file, self.local_path + '/' + file.get_name())
        stdin, stdout, stderr = self.client.exec_command(
            'rm /tmp/{0}'.format(file.get_name()))
        stdout.channel.recv_exit_status()

    def fullpath(self, file, path, appname):
        path = os.path.join(path, appname, file.path)
        return path


class RemoteFile(object):
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return self.path.split('-', 3)[3].replace('/', '-').strip()
