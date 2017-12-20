from src.domain.usecase.AnomalyFromLog import AnomalyFromLog

class LogClassifier(object):
    """
       Factory class for AnomalyFromLog use case
    """
    def __init__(self):
        self.train_repository = None
        self.test_repository = None
        self.notifier = None
        self.train_persister = None
        self.test_persister = None

    def add_train_repository(self, repository):
        self.train_repository = repository

    def add_test_repository(self, repository):
        self.test_repository = repository

    def add_notifier(self, notifier):
        self.notifier = notifier

    def add_train_persister(self, persister):
        self.train_persister = persister

    def add_test_persister(self, persister):
        self.test_persister = persister

    def compile(self):
        return AnomalyFromLog(train_repository=self.train_repository,
                              test_repository=self.test_repository,
                              notifier=self.notifier,
                              train_persister=self.train_persister,
                              test_persister=self.test_persister)

