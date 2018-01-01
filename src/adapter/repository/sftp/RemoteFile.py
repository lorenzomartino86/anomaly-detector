class RemoteFile(object):
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return self.path.split('/')[-1]

    def get_extension(self):
        return self.path.split('/')[-1].split('.')[-1]

    def get_path(self):
        return self.path
