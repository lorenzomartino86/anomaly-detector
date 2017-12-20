from src.domain.usecase.channel.Persister import Persister
import _pickle, os

class FilePersister(Persister):
    def __init__(self, file):
        self.file = file

    def get(self):
        if not os.path.isfile(self.file): raise ValueError("file not found")
        file = open(self.file, 'rb')
        return _pickle.load(file)

    def save(self, object):
        file = open(self.file, 'wb')
        _pickle.dump(object, file)
        file.close()

    def remove(self):
        if not os.path.isfile(self.file): raise ValueError("file not found")
        os.remove(self.file)
