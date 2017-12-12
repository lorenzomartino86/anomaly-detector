from src.domain.usecase.channel.Notifier import Notifier
import pika

class MessageBroker(Notifier):

    def __init__(self):
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        self.channel.basic_publish(exchange='example',
                      routing_key='test',
                      body='Test Message')
