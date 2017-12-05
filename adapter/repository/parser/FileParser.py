from domain.cosine_similarity.RawInput import RawInput
from domain.usecase.port.Parser import Parser


class FileParser(Parser):

    def parse(self, records):
        parsed_records = list()
        for row in records:
            raw = RawInput(corpus=row)
            parsed_records.append(raw)
        return parsed_records