from abc import abstractmethod

class Repository:

    @abstractmethod
    def get(self, _from, to): pass