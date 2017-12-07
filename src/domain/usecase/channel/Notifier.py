from abc import abstractmethod

class Notifier:

    @abstractmethod
    def notify(self, new_clusters): pass