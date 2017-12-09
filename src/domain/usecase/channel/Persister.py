from abc import abstractmethod

class Persister:

    @abstractmethod
    def save(self, filename, object): pass

    @abstractmethod
    def get(self, filename): pass

    @abstractmethod
    def remove(self, filename): pass