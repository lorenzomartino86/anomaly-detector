import unittest
from unittest import TestCase

from src.domain.knn.UnsupervisedNearestNeighbors import UnsupervisedNearestNeighbors


class TestUnsupervisedNearestNeighbors(TestCase):
    def test_uniform_distribution(self):
        X = [[0, 1], [2, 3], [4, 5]]
        classifier = UnsupervisedNearestNeighbors()

        x1 = [[1, 1]]
        classifier.fit(X)
        neighbors = classifier.kneighbors(x1)
        print (neighbors)
        #self.assertEqual(predicted[0], 0)


if __name__ == '__main__':
    unittest.main()
