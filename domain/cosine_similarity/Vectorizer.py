from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer(object):

    def __init__(self, stop_words='english'):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words)

    def fit(self, corpus):
        return self.vectorizer.fit_transform(corpus)