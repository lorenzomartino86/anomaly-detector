from src.domain.usecase.channel.Persister import Persister
import _pickle, os


class FilePersister(Persister):
    def __init__(self, base_path):
        self.base_path = base_path + "/"

    def get(self, filename):
        file_path = self.base_path + filename
        if not os.path.isfile(file_path): raise ValueError("file not found")
        file = open(file_path, 'rb')
        return _pickle.load(file)

    def save(self, filename, object):
        file_path = self.base_path + filename
        file = open(file_path, 'wb')
        _pickle.dump(object, file)
        file.close()

    def remove(self, filename):
        file_path = self.base_path + filename
        if not os.path.isfile(file_path): raise ValueError("file not found")
        os.remove(file_path)
