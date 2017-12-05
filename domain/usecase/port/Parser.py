from abc import abstractmethod

class Parser:

    @abstractmethod
    def parse(self, record): pass