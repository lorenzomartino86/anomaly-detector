from domain.cosine_similarity.RawInput import RawInput
from domain.usecase.port.Parser import Parser


class FileParser(Parser):

    def __init__(self, path):
        self.path = path

    def parse(self):
        file = open(self.path)
        records = list()
        for row in file:
            raw = RawInput(corpus=row)
            records.append(raw)
        return records