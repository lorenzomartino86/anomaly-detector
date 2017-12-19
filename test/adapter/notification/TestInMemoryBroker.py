import unittest

from src.adapter.notification.InMemoryBroker import InMemoryBroker


class TestInMemoryBroker(unittest.TestCase):

    def setUp(self):
        self.broker = InMemoryBroker()

    def test_single_notify(self):
        object = list()
        object.append(1)
        object.append(2)
        self.broker.notify(object)
        self.assertEqual(self.broker.queue.get(),
                         object,
                         "it should retrieve the same object pushed before")

    def test_multiple_notify(self):
        object1 = list()
        object1.append(1)
        object1.append(2)

        object2 = list()
        object2.append(1)
        object2.append(2)

        self.broker.notify(object2)
        self.broker.notify(object1)

        self.assertEqual(self.broker.queue.get(),
                         object2,
                         "it should retrieve the same object2")

        self.assertEqual(self.broker.queue.get(),
                         object1,
                         "it should retrieve the same object1")

if __name__ == '__main__':
    unittest.main()
