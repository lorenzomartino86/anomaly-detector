from src.adapter.notification.presenter.ClusterReport import ClusterReport
from src.domain.usecase.channel.Notifier import Notifier
import pika


class MessageProducer(Notifier):
    def __init__(self, host, queue, report=ClusterReport()):
        # Connection to a Broker running on the given hostname
        self.report = report
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        # Make sure the recipient queue exists
        self.channel.queue_declare(queue=queue)
        self.queue = queue

    def notify(self, new_clusters):
        message = self.report.prepare(new_clusters)

        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

        self.connection.close()
