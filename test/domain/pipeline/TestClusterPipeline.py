import unittest

from domain.cosine_similarity.ClusterSimilarity import ClusterSimilarity
from domain.cosine_similarity.RawInput import RawInput
from domain.pipeline.ClusterPipeline import ClusterPipeline

class TestClusterPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = ClusterPipeline()

    def test_no_new_cluster(self):
        train_raw = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        test_raw = [RawInput(corpus="Hello world!")]

        detected_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        self.assertEqual(len(detected_clusters), 0, "no cluster should be detected")

    def test_one_new_cluster(self):
        train_raw = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        test_raw = [RawInput(corpus="Jeepers creepers for ever and ever")]

        detected_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        self.assertEqual(len(detected_clusters), 1, "one cluster should be detected")

if __name__ == '__main__':
    unittest.main()
