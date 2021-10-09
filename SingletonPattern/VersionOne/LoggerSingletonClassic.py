import datetime

class Logger(object):
    logFile = None

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance

    def openLog(self, path):
        self.logFile = open(path, mode='w')

    def writeLog(self, logRecord):
        now = str(datetime.datetime.now())
        record = '%s: %s' % (now, logRecord)
        self.logFile.writelines(record)

    def closeLog(self):
        self.logFile.close()