from src.domain.pipeline.ClusterPipeline import ClusterPipeline
import datetime

class AnomalyFromLog(object):

    def __init__(self, train_repository, test_repository, notifier, persister):
        self.persister = persister
        self.notifier = notifier
        self.pipeline = ClusterPipeline()
        self.train_repository = train_repository
        self.test_repository = test_repository
        today = datetime.datetime.today()
        self.today_cluster_filename = "clusters_" + today.strftime('%Y-%m-%d') + ".obj"

    def detect_anomaly(self):

        # get train and test set
        train_raw = self.train_repository.get()
        test_raw = self.test_repository.get()

        # cluster pipeline
        new_clusters = self.pipeline.detect(train_raw=train_raw,
                                            test_raw=test_raw)

        # notifications
        self.notifier.notify(new_clusters)

        # clusters persistence
        self.persister.save(filename=self.today_cluster_filename, object=new_clusters)

        return new_clusters

