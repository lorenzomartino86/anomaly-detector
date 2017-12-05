from abc import abstractmethod

class Persister:

    @abstractmethod
    def save(self, id, train_clusters): pass

    @abstractmethod
    def get(self, id): pass