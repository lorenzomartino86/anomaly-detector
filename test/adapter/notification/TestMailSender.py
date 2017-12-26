import unittest
from unittest import TestCase

from src.adapter.notification.MailSender import MailSender
from unittest.mock import patch, call

class TestMailSender(TestCase):

    def test_mail(self):
        # Mocking 'smtplib.SMTP' class
        _from = "from@domain.com"
        to = "to@domain.com"
        server = "server.intra"
        subject = "mocked mail test"

        with patch("smtplib.SMTP") as mock_smtp:

            sender = MailSender(server=server, _from=_from,
                                to=to, subject=subject)

            object = list()
            object.append("HELLO WORLD")
            object.append("BAD BAD BOY")

            sender.notify(object)

        # Get instance of mocked SMTP object
        instance = mock_smtp.return_value

        # Checks the mock has been called at least one time
        self.assertTrue(instance.sendmail.called)

        # Check the mock has been called only once
        self.assertEqual(instance.sendmail.call_count, 1)


if __name__ == '__main__':
    unittest.main()


