from src.domain.usecase.AnomalyFromLog import AnomalyFromLog

class LogClassifier(object):

    def __init__(self):
        self.repository = None
        self.notifier = None
        self.persister = None

    def add_repository(self, repository):
        self.repository = repository

    def add_notifier(self, notifier):
        self.notifier = notifier

    def add_persister(self, persister):
        self.persister = persister

    def compile(self):
        return AnomalyFromLog(repository=self.repository,
                              notifier=self.notifier,
                              persister=self.persister)

