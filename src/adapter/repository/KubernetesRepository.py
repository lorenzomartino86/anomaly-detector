from src.adapter.repository.parser.SimpleParser import SimpleParser
from src.domain.usecase.channel.Repository import Repository

class InMemoryRepository(Repository):

    def __init__(self, data, parser=SimpleParser()):
        self.data = data
        self.parser = parser

    def get(self):
        return self.parser.parse(self.data)