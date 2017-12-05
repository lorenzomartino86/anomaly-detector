class RawInput(object):

    def __init__(self, corpus):
        self.corpus = corpus

    def __repr__(self):
        return str(self.get_dict())

    def get_dict(self):
        return {'corpus': self.corpus}