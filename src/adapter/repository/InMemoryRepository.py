from src.adapter.repository.parser.FileParser import SimpleParser
from src.domain.usecase.channel.Repository import Repository

class InMemoryRepository(Repository):

    def __init__(self, data):
        self.data = data

    def get(self):
        return self.data