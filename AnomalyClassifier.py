from src.domain.usecase.AnomalyFromLog import AnomalyFromLog

class LogClassifier(object):
    """
       Factory class for AnomalyFromLog use case
    """
    def __init__(self):
        self.train_repository = None
        self.test_repository = None
        self.notifier = None
        self.persister = None

    def add_train_repository(self, repository):
        self.train_repository = repository

    def add_test_repository(self, repository):
        self.test_repository = repository

    def add_notifier(self, notifier):
        self.notifier = notifier

    def add_persister(self, persister):
        self.persister = persister

    def compile(self):
        return AnomalyFromLog(train_repository=self.train_repository,
                              test_repository=self.test_repository,
                              notifier=self.notifier,
                              persister=self.persister)

