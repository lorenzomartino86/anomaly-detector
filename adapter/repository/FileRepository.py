from adapter.repository.parser.FileParser import FileParser
from domain.usecase.port.Repository import Repository


class FileRepository(Repository):

    def __init__(self, path):
        self.path = path
        self.parser = FileParser(path)

    def get(self, _from, to):
        return self.parser.parse()