from src.domain.usecase.AnomalyFromLog import AnomalyFromLog

class LogClassifier(object):
    """
       Factory class for AnomalyFromLog use case
    """
    def __init__(self, train_repository, test_repository, notifier):
        self.train_repository = train_repository
        self.test_repository = test_repository
        self.notifier = notifier
        self.train_persister = None
        self.outlier_persister = None

    def add_train_persister(self, persister):
        self.train_persister = persister

    def add_outlier_persister(self, persister):
        self.outlier_persister = persister

    def compile(self):
        return AnomalyFromLog(train_repository=self.train_repository,
                              test_repository=self.test_repository,
                              notifier=self.notifier,
                              train_persister=self.train_persister,
                              outlier_persister=self.outlier_persister)

