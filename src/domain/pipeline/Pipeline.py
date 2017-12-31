from abc import abstractmethod


class Pipeline:

    @abstractmethod
    def detect(self, train_raw, test_raw): pass
