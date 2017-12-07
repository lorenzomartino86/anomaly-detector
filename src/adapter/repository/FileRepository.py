from src.adapter.repository.parser.FileParser import FileParser
from src.domain.usecase.channel.Repository import Repository


class FileRepository(Repository):

    def __init__(self, train_path, test_path):
        self.train_records = open(train_path)
        self.test_records = open(test_path)
        self.parser = FileParser()

    def get(self):
        train_records, test_records = self.parser.parse(self.train_records), \
                                      self.parser.parse(self.test_records)
        self.train_records.close()
        self.test_records.close()
        return train_records, test_records