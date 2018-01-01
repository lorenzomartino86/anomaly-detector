import paramiko

from src.adapter.repository.sftp.RemoteFile import RemoteFile
from src.decorator.logging import exception


class SSHClient(object):
    def __init__(self, ssh_key_file, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(hostname=hostname, username=username, compress=True,
                            key_filename=ssh_key_file, password=password)

    @exception
    def copy(self, from_file, to_file):
        print (from_file, to_file)
        print ('cp {0} {1}'.format(from_file, to_file))
        self.client.exec_command('cp {0} {1}'.format(from_file, to_file))

    @exception
    def remove(self, file):
        self.client.exec_command('rm {0}'.format(file))

    @exception
    def sftp_session(self, remote_file, local_file):
        session = self.client.open_sftp()
        try:
            session.get(remote_file, local_file)
        finally:
            session.close()

    @exception
    def disconnect(self):
        self.client.disconnect()