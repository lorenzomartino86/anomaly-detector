from sklearn.neighbors import NearestNeighbors


class UnsupervisedNearestNeighbors(object):
    def __init__(self, neighbors=3):
        self.neighbors = neighbors
        self.classifier = NearestNeighbors(n_neighbors=neighbors)

    def fit(self, X):
        self.classifier.fit(X)

    def kneighbors(self, x):
        return self.classifier.kneighbors(X=x, n_neighbors=self.neighbors, return_distance=True)
