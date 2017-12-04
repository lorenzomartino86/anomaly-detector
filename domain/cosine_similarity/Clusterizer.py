from sklearn.feature_extraction.text import TfidfVectorizer
from decorator.time import elapsed_time
from domain.cosine_similarity.Cluster import Cluster
from domain.cosine_similarity.CosineSimilarity import CosineSimilarity
from domain.cosine_similarity.Vectorizer import Vectorizer

class Clusterizer(object):

    def __init__(self, stop_words='english', ratio=.98):
        self.vectorizer = Vectorizer(stop_words=stop_words)
        self.similarity = CosineSimilarity(ratio=ratio)

    @elapsed_time
    def clusterize(self, records):
        corpus = [record.corpus for record in records]

        if len(corpus) == 0: return list()

        X = self.vectorizer.fit(corpus)

        clusters = list()
        for record in range(0, X.shape[0]):
            clustered = False
            for cluster in clusters:
                if self.similarity.is_similar(X=X[record], Y=cluster.centroid):
                    cluster.records.append(records[record])
                    cluster.centroid = (cluster.centroid + X[record]) / 2
                    clustered = True
                    break
            if not clustered:
                new_cluster = Cluster(records=[records[record]], centroid=X[record])
                clusters.append(new_cluster)

        return clusters
