class ClusterReport(object):

    def prepare(self, records):
        report = str()
        for record in records:
            report += "<b>[record-" + record + ":<span style=\"color: #ff0000\">"
        return report
