from src.adapter.repository.parser.FileParser import FileParser
from src.domain.usecase.channel.Repository import Repository

class FileRepository(Repository):

    def __init__(self, train_file, test_file):
        self.train_records = train_file
        self.test_records = test_file
        self.parser = FileParser()

    def get(self):
        train_records, test_records = self.parser.parse(self.train_records), \
                                      self.parser.parse(self.test_records)
        self.train_records.close()
        self.test_records.close()
        return train_records, test_records