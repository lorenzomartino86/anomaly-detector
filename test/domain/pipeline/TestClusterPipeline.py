import unittest

from src.domain.cosine_similarity.RawInput import RawInput
from src.domain.pipeline.ClusterPipeline import ClusterPipeline


class TestClusterPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = ClusterPipeline()

    def test_no_new_cluster(self):
        train_raw = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        test_raw = [RawInput(corpus="Hello world!"),
                    RawInput(corpus="Hello"),
                    RawInput(corpus="world"),
                    RawInput(corpus="Hello world")]

        new_clusters, train_clusters, test_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        self.assertEqual(len(new_clusters), 0, "any new cluster should be detected")

    def test_one_new_cluster(self):
        train_raw = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        test_raw = [RawInput(corpus="Jeepers creepers for ever and ever")]

        new_clusters, train_clusters, test_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        self.assertEqual(len(new_clusters), 1, "one new cluster should be detected")


    def test_multiple_new_clusters(self):
        train_raw = [RawInput(corpus="Hello world!"),
                     RawInput(corpus="Hello world!")]
        test_raw = [RawInput(corpus="Jeepers creepers for ever and ever"),
                    RawInput(corpus="Jeepers creepers"),
                    RawInput(corpus="Mountain sea lake"),
                    RawInput(corpus="star wars the revenge")]

        new_clusters, train_clusters, test_clusters = self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

        self.assertEqual(len(new_clusters), 3, "three new clusters should be detected")


if __name__ == '__main__':
    unittest.main()
