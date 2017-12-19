from src.domain.usecase.channel.Notifier import Notifier
import pika

class MessageBroker(Notifier):

    def __init__(self, host, queue):
        # Connection to a Broker running on the given hostname
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        # Make sure the recipient queue exists
        self.channel.queue_declare(queue=queue)
        self.queue = queue

    def notify(self, new_clusters):
        message = str()

        for cluster in new_clusters:
            message += cluster.records

        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

        self.connection.close()


