from queue import Queue

from src.domain.usecase.channel.Notifier import Notifier

class InMemoryBroker(Notifier):

    def __init__(self):
        self.queue = Queue()

    def notify(self, new_clusters):
        self.queue.put(new_clusters)