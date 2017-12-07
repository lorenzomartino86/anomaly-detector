from sklearn.feature_extraction.text import TfidfVectorizer

class TextProcessor(object):

    def __init__(self, stop_words='english'):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words)

    def transform(self, records):
        if len(records) == 0: raise ValueError
        corpus = [record.corpus for record in records]
        return self.vectorizer.fit_transform(corpus)