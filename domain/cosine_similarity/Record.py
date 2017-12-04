class Record(object):

    def __init__(self, server=None, datetime=None, trackid=None, level=None, message=None, corpus=None):
        self.server = server
        self.datetime = datetime
        self.trackid = trackid
        self.level = level
        self.message = message
        self.corpus = corpus

    def __repr__(self):
        return str(self.get_dict())

    def get_dict(self):
        return {'datetime': self.datetime,
                'server': self.server,
                'level': self.level,
                'message': self.message,
                'corpus': self.corpus,
                'trackid': self.trackid}