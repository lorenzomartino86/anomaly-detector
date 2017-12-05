import unittest

from domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from domain.cosine_similarity.Clusterizer import Clusterizer
from domain.cosine_similarity.RawInput import RawInput

class TestClusterSimilarity(unittest.TestCase):

    def setUp(self):
        self.clusterizer = Clusterizer()


if __name__ == '__main__':
    unittest.main()
