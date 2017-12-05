from domain.cosine_similarity.CosineSimilarity import CosineSimilarity


class ClusterSimilarity(object):

    def __init__(self, train_clusters, ratio=.98):
        self.similarity = CosineSimilarity(ratio=ratio)
        self.train_clusters = train_clusters

    def is_new_cluster(self, cluster):
        similarities = [self.similarity.is_similar(train_cluster.centroid, cluster.centroid)
                        for train_cluster in self.train_clusters]
        return similarities.count(True) == 0