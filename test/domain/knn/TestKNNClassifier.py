import unittest
from unittest import TestCase

from src.domain.knn.KNNClassifier import KNNClassifier


class TestKNNClassifier(TestCase):
    def test_uniform_distribution(self):
        X = [[0], [1], [2], [3], [4], [5]]
        y = [0, 1, 2, 0, 1, 2]
        classifier = KNNClassifier(X, y)

        x1 = [1.1]
        predicted = classifier.predict(x1)
        probability = classifier.probability(x1)
        self.assertEqual(predicted[0], 0)
        self.assertEqual(probability[0][0], 0.33333333333333331)
        self.assertEqual(probability[0][1], 0.33333333333333331)
        self.assertEqual(probability[0][2], 0.33333333333333331)

        x2 = [5.1]
        predicted = classifier.predict(x2)
        probability = classifier.probability(x2)
        self.assertEqual(predicted[0], 0)
        self.assertEqual(probability[0][0], 0.33333333333333331)
        self.assertEqual(probability[0][1], 0.33333333333333331)
        self.assertEqual(probability[0][2], 0.33333333333333331)

    def test_sparse_distribution(self):
        X = [[0], [1], [2], [3], [4], [5]]
        y = [2, 1, 1, 0, 0, 2]
        classifier = KNNClassifier(X, y)

        x1 = [1.1]
        predicted = classifier.predict(x1)
        probability = classifier.probability(x1)
        self.assertEqual(predicted[0], 1)
        self.assertEqual(probability[0][0], 0.0)
        self.assertEqual(probability[0][1], 0.66666666666666663)
        self.assertEqual(probability[0][2], 0.33333333333333331)

        x2 = [5.1]
        predicted = classifier.predict(x2)
        probability = classifier.probability(x2)
        self.assertEqual(predicted[0], 0)
        self.assertEqual(probability[0][0], 0.66666666666666663)
        self.assertEqual(probability[0][1], 0.0)
        self.assertEqual(probability[0][2], 0.33333333333333331)

    def test_one_neighbor(self):
        X = [[0], [1], [2], [3], [4], [5]]
        y = [2, 1, 1, 0, 0, 2]
        classifier = KNNClassifier(X, y, neighbors=1)

        x1 = [1.1]
        predicted = classifier.predict(x1)
        probability = classifier.probability(x1)
        self.assertEqual(predicted[0], 1)
        self.assertEqual(probability[0][0], 0.0)
        self.assertEqual(probability[0][1], 1.0)
        self.assertEqual(probability[0][2], 0.0)

        x2 = [5.1]
        predicted = classifier.predict(x2)
        probability = classifier.probability(x2)
        self.assertEqual(predicted[0], 2)
        self.assertEqual(probability[0][0], 0.0)
        self.assertEqual(probability[0][1], 0.0)
        self.assertEqual(probability[0][2], 1.0)

    def test_multiple_neighbors(self):
        X = [[0], [1], [2], [3], [4], [5]]
        y = [2, 1, 3, 5, 4, 0]
        classifier = KNNClassifier(X, y, neighbors=6)

        x1 = [1.1]
        predicted = classifier.predict(x1)
        probability = classifier.probability(x1)
        self.assertEqual(predicted[0], 0)
        self.assertEqual(probability[0][0], 0.16666666666666666)
        self.assertEqual(probability[0][1], 0.16666666666666666)
        self.assertEqual(probability[0][2], 0.16666666666666666)
        self.assertEqual(probability[0][3], 0.16666666666666666)
        self.assertEqual(probability[0][4], 0.16666666666666666)
        self.assertEqual(probability[0][5], 0.16666666666666666)

        x2 = [5.1]
        predicted = classifier.predict(x2)
        probability = classifier.probability(x2)
        self.assertEqual(predicted[0], 0)
        self.assertEqual(probability[0][0], 0.16666666666666666)
        self.assertEqual(probability[0][1], 0.16666666666666666)
        self.assertEqual(probability[0][2], 0.16666666666666666)
        self.assertEqual(probability[0][3], 0.16666666666666666)
        self.assertEqual(probability[0][4], 0.16666666666666666)
        self.assertEqual(probability[0][5], 0.16666666666666666)


if __name__ == '__main__':
    unittest.main()
