from sklearn.metrics.pairwise import cosine_similarity


class CosineSimilarity(object):
    def __init__(self, ratio=.98):
        self.ratio = ratio

    def is_similar(self, X, Y):
        return cosine_similarity(X, Y) > self.ratio
