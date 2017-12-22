from src.adapter.repository.parser.FileParser import SimpleParser
from src.domain.usecase.channel.Repository import Repository

class FileRepository(Repository):

    def __init__(self, file, parser=SimpleParser()):
        self.file = file
        self.parser = parser

    def get(self):
        records = self.parser.parse(self.file)
        self.file.close()
        return records