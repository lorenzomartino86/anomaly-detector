from sklearn.neighbors import KNeighborsClassifier

from src.decorator.logging import exception


class KNNClassifier(object):
    def __init__(self, X, y, neighbors=3):
        self.classifier = KNeighborsClassifier(n_neighbors=neighbors)
        self.classifier.fit(X, y)

    @exception
    def predict(self, x):
        return self.classifier.predict(x)

    @exception
    def probability(self, x):
        return self.classifier.predict_proba(x)
