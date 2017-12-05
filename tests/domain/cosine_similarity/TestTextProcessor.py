import unittest

from domain.cosine_similarity.RawInput import RawInput
from domain.cosine_similarity.TextProcessor import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.textProcessor = TextProcessor()

    def test_simple_text_processing(self):
        x = [RawInput(corpus="Hello world!")]
        xTransformed = self.textProcessor.transform(x)
        self.assertEqual(xTransformed.shape, (1,2))

    def test_complex_text_processing(self):
        x = [RawInput(corpus="Hello world of my God on the mountain sea!"),
             RawInput(corpus="Pippo pluto paperina")]
        xTransformed = self.textProcessor.transform(x)
        self.assertEqual(xTransformed.shape, (2,8))

if __name__ == '__main__':
    unittest.main()
