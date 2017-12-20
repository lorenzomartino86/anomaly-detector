from src.decorator.logging import exception
from src.domain.pipeline.ClusterPipeline import ClusterPipeline

class AnomalyFromLog(object):

    def __init__(self, train_repository, test_repository, notifier, train_persister, test_persister):
        self.test_persister = test_persister
        self.train_persister = train_persister
        self.notifier = notifier
        self.pipeline = ClusterPipeline()
        self.train_repository = train_repository
        self.test_repository = test_repository

    @exception
    def detect_anomaly(self):

        # get train and test set
        train_raw = self.train_repository.get()

        test_raw = self.test_repository.get()

        # cluster pipeline
        new_clusters, train_clusters, test_clusters = self.pipeline.detect(train_raw=train_raw,
                                            test_raw=test_raw)

        # notifications
        self.notifier.notify(new_clusters)

        # clusters persistence
        if self.test_persister is not None:
            self.test_persister.save(object=new_clusters)

        return new_clusters

