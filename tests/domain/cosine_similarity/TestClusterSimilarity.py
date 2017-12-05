import unittest

from domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from domain.cosine_similarity.Clusterizer import Clusterizer
from domain.cosine_similarity.RawInput import RawInput

class TestClusterSimilarity(unittest.TestCase):

    def setUp(self):
        self.clusterizer = Clusterizer()

    def test_similarity_for_same_clusters(self):
        x = [RawInput(corpus="Hello world!")]
        y = [RawInput(corpus="Hello world!")]
        xCluster = self.clusterizer.clusterize(dataset=x)
        yCluster = self.clusterizer.clusterize(dataset=y)
        similarity = ClusterSimilarity(train_clusters=xCluster, ratio=.70)
        self.assertEqual(similarity.is_new_cluster(yCluster[0]), False, "x and y should have same cluster")

    def test_similarity_for_different_clusters(self):
        x = [RawInput(corpus="Hello world!")]
        y = [RawInput(corpus="Moon in my morning God")]
        xCluster = self.clusterizer.clusterize(records=x)
        yCluster = self.clusterizer.clusterize(records=y)
        similarity = ClusterSimilarity(train_clusters=xCluster, ratio=.70)
        self.assertEqual(similarity.is_new_cluster(yCluster[0]), False, "x and y should have different cluster")

    def test_similarity_for_similar_records(self):
        x = "Hello my world"
        y = "Hello my world of God"

if __name__ == '__main__':
    unittest.main()
