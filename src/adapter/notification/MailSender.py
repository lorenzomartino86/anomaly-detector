import smtplib
from email.mime.text import MIMEText
from datetime import datetime

from src.adapter.notification.presenter.ClusterReport import ClusterReport
from src.decorator.logging import exception
from src.domain.usecase.channel.Notifier import Notifier


class MailSender(Notifier):

    def __init__(self, server, _from, to, subject, username, password, report=ClusterReport()):
        self.server = smtplib.SMTP(server)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)
        self.subject = subject
        self.to = to
        self._from = _from
        self.report = report

    @exception
    def notify(self, new_clusters):
        text_subtype = 'html'

        text = self.report.prepare(new_clusters)
        content = """<html>
                <head></head>
                <body>
                <p><b>Clustering Output</b>
                <br><br>
                <b>Datetime: </b>{0}
                </p>
                <br>
                {1}
                </body>
                </html>""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text)

        message = MIMEText(content, text_subtype)
        message['Subject'] = self.subject
        message['From'] = self._from
        self.server.sendmail(self._from, self.to, message.as_string())
        self.server.quit()

    def get_clusters_reports(clusters):
        reporter = ClusterReport()
        clusters_reports = []
        for cluster in clusters:
            clusters_reports.append(reporter.get_report_for(cluster))
        return clusters_reports
