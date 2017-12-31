from src.domain.cosine_similarity.TextProcessor import TextProcessor
from src.domain.pipeline.Pipeline import Pipeline


class KNNPipeline(Pipeline):
    def __init__(self):
        self.textProcessor = TextProcessor()

    def detect(self, train_raw, test_raw):
        if train_raw is None or test_raw is None: raise ValueError
        train_card, test_card = len(train_raw), len(test_raw)
        dataset_raw = train_raw + test_raw
        dataset_vector = self.textProcessor.transform(dataset_raw)
        train_dataset = dataset_vector[:train_card - 1]
        test_dataset = dataset_vector[train_card:]
        print(train_dataset, test_dataset)







