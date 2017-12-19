from src.adapter.repository.parser.FileParser import FileParser
from src.domain.usecase.channel.Repository import Repository

class FileRepository(Repository):

    def __init__(self, file):
        self.file = file
        self.parser = FileParser()

    def get(self):
        records = self.parser.parse(self.file)
        self.file.close()
        return records