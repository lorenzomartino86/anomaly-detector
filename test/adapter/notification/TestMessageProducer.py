import unittest
from unittest import TestCase
from unittest.mock import patch, call

from src.adapter.notification.MessageProducer import MessageProducer


class TestMessageProducer(TestCase):

    def test_single_message(self):

        with patch("pika.BlockingConnection") as mock_pika:
            producer = MessageProducer(host='127.0.0.1', queue='mock-queue')

            object = list()
            object.append("HELLO WORLD")
            object.append("BAD BAD BOY")
            producer.notify(object)

        # Get instance of mocked PIKA object
        instance = mock_pika.return_value
        channel = instance.channel.return_value

        # Checks the mock has been called at least one time
        self.assertTrue(channel.basic_publish.called)

        # Check the mock has been called only once
        self.assertEqual(channel.basic_publish.call_count, 1)


if __name__ == '__main__':
    unittest.main()
