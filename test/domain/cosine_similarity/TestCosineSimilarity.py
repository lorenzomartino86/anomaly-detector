import unittest

from domain.cosine_similarity.CosineSimilarity import CosineSimilarity
from domain.cosine_similarity.RawInput import RawInput
from domain.cosine_similarity.TextProcessor import TextProcessor


class TestCosineSimilarity(unittest.TestCase):

    def setUp(self):
        self.similarity = CosineSimilarity(ratio=.70)
        self.textProcessor = TextProcessor()

    def test_similarity_for_same_records(self):
        x = RawInput(corpus="Hello world!")
        y = RawInput(corpus="Hello world!")
        records = self.textProcessor.transform([x, y])
        self.assertEqual(self.similarity.is_similar(records[0], records[1]), True, "x and y should be similar")

    def test_similarity_for_different_records(self):
        x = RawInput(corpus="Hello world!")
        y = RawInput(corpus="Moon in my morning God")
        records = self.textProcessor.transform([x, y])
        self.assertEqual(self.similarity.is_similar(records[0], records[1]), False, "x and y should not be similar")

    def test_similarity_for_similar_records(self):
        x = RawInput(corpus="Hello my world")
        y = RawInput(corpus="Hello my world of God")
        records = self.textProcessor.transform([x, y])
        self.assertEqual(self.similarity.is_similar(records[0], records[1]), True, "x and y should be similar")

if __name__ == '__main__':
    unittest.main()
