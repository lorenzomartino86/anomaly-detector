from src.decorator.time import elapsed_time
from src.domain.cosine_similarity.Cluster import Cluster
from src.domain.cosine_similarity.CosineSimilarity import CosineSimilarity


class ClusterGenerator(object):

    def __init__(self, ratio=.98):
        self.similarity = CosineSimilarity(ratio=ratio)

    @elapsed_time
    def clusterize(self, dataset, raw_input):
        clusters = list()
        for record in range(0, dataset.shape[0]):
            clustered = False
            for cluster in clusters:
                if self.similarity.is_similar(X=dataset[record], Y=cluster.centroid):
                    cluster.records.append(raw_input[record])
                    cluster.centroid = (cluster.centroid + dataset[record]) / 2
                    clustered = True
                    break
            if not clustered:
                new_cluster = Cluster(records=[raw_input[record]],
                                      centroid=dataset[record])
                clusters.append(new_cluster)
        return clusters
