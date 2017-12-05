from abc import abstractmethod

class Repository:

    @abstractmethod
    def get(self, parser, _from, to): pass