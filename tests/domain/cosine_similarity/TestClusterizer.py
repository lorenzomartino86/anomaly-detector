import unittest

from domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from domain.cosine_similarity.Clusterizer import Clusterizer
from domain.cosine_similarity.RawInput import RawInput
from domain.cosine_similarity.TextProcessor import TextProcessor


class TestClusterSimilarity(unittest.TestCase):

    def setUp(self):
        self.clusterizer = Clusterizer()
        self.textProcessor = TextProcessor()

    def test_one_cluster(self):
        raw_input = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        dataset = self.textProcessor.transform(raw_input)
        clusters = self.clusterizer.clusterize(dataset=dataset, raw_input=raw_input)
        self.assertEqual(len(clusters), 1, "only 1 cluster is admitted")

    def test_two_clusters(self):
        raw_input = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="I like the sea")]
        dataset = self.textProcessor.transform(raw_input)
        clusters = self.clusterizer.clusterize(dataset=dataset, raw_input=raw_input)
        self.assertEqual(len(clusters), 2, "only 2 clusters are admitted")

    def test_multiple_clusters(self):
        raw_input = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="I like the sea"),
                     RawInput(corpus="I like the sea"),
                     RawInput(corpus="On the Autumn Leaves"),
                     RawInput(corpus="Hello world!")]
        dataset = self.textProcessor.transform(raw_input)
        clusters = self.clusterizer.clusterize(dataset=dataset, raw_input=raw_input)
        self.assertEqual(len(clusters), 3, "only 3 clusters are admitted")

if __name__ == '__main__':
    unittest.main()
