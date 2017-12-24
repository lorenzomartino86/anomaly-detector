class ClusterReport(object):

    def prepare(self, clusters):
        report = str()
        for cluster in clusters:
            for record in cluster.records:
                record += "<b>[record-" + record + ":<span style=\"color: #ff0000\">"
        return report
