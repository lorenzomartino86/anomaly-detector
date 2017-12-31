import unittest
from unittest import TestCase

from src.domain.cosine_similarity.RawInput import RawInput
from src.domain.pipeline.KNNPipeline import KNNPipeline


class TestKNNPipeline(TestCase):
    def setUp(self):
        self.pipeline = KNNPipeline()

    def test_detect_outlier(self):
        train_raw = list()
        train_raw.append(RawInput(corpus="Hello World"))
        train_raw.append(RawInput(corpus="Uncle Bob"))

        test_raw = list()
        test_raw.append(RawInput(corpus="This is an outlier"))
        test_raw.append(RawInput(corpus="Hello World"))

        self.pipeline.detect(train_raw=train_raw, test_raw=test_raw)

if __name__ == '__main__':
    unittest.main()

