import paramiko

from src.adapter.repository.sftp.RemoteFile import RemoteFile


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