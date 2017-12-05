from adapter.repository import FileRepository
from domain.pipeline.ClusterPipeline import ClusterPipeline


class LogDetector(object):

    def __init__(self, repository=FileRepository):
        self.pipeline = ClusterPipeline()
        self.repository = repository


    def detect_anomaly(self):

        # get train raw


        # get test raw

        # cluster pipeline

        # notifications

        pass

