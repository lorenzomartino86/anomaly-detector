import unittest

from domain.cosine_similarity.CosineSimilarity import CosineSimilarity
from domain.cosine_similarity.Vectorizer import Vectorizer

class TestCosineSimilarity(unittest.TestCase):

    def setUp(self):
        self.similarity = CosineSimilarity(ratio=.70)

    def test_similarity_for_same_records(self):
        x = "Hello world!"
        y = "Hello world!"
        vectorizer = Vectorizer()
        vectorized = vectorizer.fit([x, y])
        self.assertEqual(self.similarity.is_similar(vectorized[0], vectorized[1]), True, "x and y should be similar")

    def test_similarity_for_different_records(self):
        x = "Hello world!"
        y = "Moon in my morning God"
        vectorizer = Vectorizer()
        vectorized = vectorizer.fit([x, y])
        self.assertEqual(self.similarity.is_similar(vectorized[0], vectorized[1]), False, "x and y should not be similar")

    def test_similarity_for_similar_records(self):
        x = "Hello my world"
        y = "Hello my world of God"
        vectorizer = Vectorizer()
        vectorized = vectorizer.fit([x, y])
        self.assertEqual(self.similarity.is_similar(vectorized[0], vectorized[1]), True, "x and y should be similar")

if __name__ == '__main__':
    unittest.main()
