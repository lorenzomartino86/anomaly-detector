from sklearn.feature_extraction.text import TfidfVectorizer

class TextProcessor(object):

    def __init__(self, stop_words='english'):
        """
        Using TfIDF vectorizer that uses Tf (Term Frequency) and IDF (Inverse document frequency)
                   tfidf(t, d, D) = tf(t, d) * idf(t, D)
        where:
            - tf(t, D) = count(t, d) / |d|
            - idf(t, D) = log(|D| / |{d in D : t in d}|)
        :param stop_words: by default 'english'
        """
        self.vectorizer = TfidfVectorizer(stop_words=stop_words)

    def transform(self, records):
        if len(records) == 0: raise ValueError
        corpus = [record.corpus for record in records]
        return self.vectorizer.fit_transform(corpus)