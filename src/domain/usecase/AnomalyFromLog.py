from src.domain.pipeline.ClusterPipeline import ClusterPipeline

class LogDetector(object):

    def __init__(self, repository):
        self.pipeline = ClusterPipeline()
        self.repository = repository

    def detect_anomaly(self):

        # get train and test set
        train_raw, test_raw = self.repository.get()

        # cluster pipeline
        new_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        # notifications

        return new_clusters

