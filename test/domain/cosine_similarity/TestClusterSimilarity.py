import unittest

from src.domain.cosine_similarity.ClusterGenerator import ClusterGenerator
from src.domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from src.domain.cosine_similarity.RawInput import RawInput
from src.domain.cosine_similarity.TextProcessor import TextProcessor


class TestClusterSimilarity(unittest.TestCase):

    def setUp(self):
        self.clusterizer = ClusterGenerator()
        self.textProcessor = TextProcessor()

    def test_no_new_cluster(self):
        raw_input = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        dataset = self.textProcessor.transform(raw_input)
        train_clusters = self.clusterizer.clusterize(dataset=dataset, raw_input=raw_input)

        clusterSimilarity = ClusterSimilarity(train_clusters=train_clusters)

        raw_input = [RawInput(corpus="Hello world!")]
        dataset = self.textProcessor.transform(raw_input)
        cluster = self.clusterizer.clusterize(dataset=dataset, raw_input=raw_input)[0]

        self.assertEqual(clusterSimilarity.is_new_cluster(cluster), False, "no new cluster to be detected")

    def test_one_new_cluster(self):
        raw_input = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!"),
                     RawInput(corpus="Jeepers creepers for ever and ever")]
        dataset = self.textProcessor.transform(raw_input)
        train_clusters = self.clusterizer.clusterize(dataset=dataset[0:1], raw_input=raw_input[0:1])

        clusterSimilarity = ClusterSimilarity(train_clusters=train_clusters)

        cluster = self.clusterizer.clusterize(dataset=dataset[2], raw_input=[raw_input[2]])[0]
        self.assertEqual(clusterSimilarity.is_new_cluster(cluster), True, "one new cluster should be detected")


if __name__ == '__main__':
    unittest.main()
