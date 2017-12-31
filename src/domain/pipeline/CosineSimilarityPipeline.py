from src.domain.cosine_similarity.ClusterGenerator import ClusterGenerator
from src.domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from src.domain.cosine_similarity.TextProcessor import TextProcessor
from src.domain.pipeline.Pipeline import Pipeline


class CosineSimilarityPipeline(Pipeline):

    def __init__(self, ratio=.70):
        self.ratio=ratio
        self.textProcessor = TextProcessor()
        self.clusterGenerator = ClusterGenerator(ratio=ratio)

    def detect(self, train_raw=None, test_raw=None):
        if train_raw is None or test_raw is None: raise ValueError

        train_card, test_card = len(train_raw), len(test_raw)
        dataset_raw = train_raw + test_raw
        dataset_vector = self.textProcessor.transform(dataset_raw)

        train_dataset = dataset_vector[:train_card-1]
        test_dataset = dataset_vector[train_card:]

        train_clusters = self.clusterGenerator.clusterize(train_dataset, train_raw)
        test_clusters = self.clusterGenerator.clusterize(test_dataset, test_raw)

        similarity = ClusterSimilarity(train_clusters=train_clusters, ratio=self.ratio)

        new_clusters=list()
        for test_cluster in test_clusters:
            if similarity.is_new_cluster(test_cluster):
                new_clusters.append(test_cluster)

        return new_clusters, train_clusters, test_clusters

