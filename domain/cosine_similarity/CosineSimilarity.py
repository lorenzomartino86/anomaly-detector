from sklearn.metrics.pairwise import cosine_similarity

class CosineSimilarity(object):

    def __init__(self, ratio=.98):
        self.ratio = ratio

    def is_similar(self, X, Y):
        print (cosine_similarity(X, Y))
        return cosine_similarity(X, Y) > self.ratio

    def detect_new_clusters(self, train, test):
        similarities = self._generate_matrix_similarities(train, test)
        new_clusters = [cluster for cluster in similarities if self._no_similarity(cluster)]
        return new_clusters


    def _generate_matrix_similarities(self, train, test):
        similarities = dict()
        for train_cluster in train:
            similarities[train_cluster] = [self.is_similar(train_cluster.centroid,
                                                             test_cluster.centroid)
                                           for test_cluster in test]
        return similarities

    def _no_similarity(self, cluster):
        return cluster.count(True) == 0


