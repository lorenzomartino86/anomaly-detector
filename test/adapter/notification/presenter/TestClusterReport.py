import unittest
from unittest import TestCase

from src.adapter.notification.presenter.ClusterReport import ClusterReport


class TestClusterReport(TestCase):
    def setUp(self):
        self.clusterReport = ClusterReport()

    def test_prepare(self):
        records = list()
        records.append("HELLO WORLD")
        records.append("BAD BAD BOY")

        cluster_report = "<b>[record-" + records[0] + ":<span style=\"color: #ff0000\">" \
                         + "<b>[record-" + records[1] + ":<span style=\"color: #ff0000\">"

        self.assertEqual(self.clusterReport.prepare(records), cluster_report)


if __name__ == '__main__':
    unittest.main()
