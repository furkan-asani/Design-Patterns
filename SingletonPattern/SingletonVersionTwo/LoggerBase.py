from SingletonBase import Singleton
import datetime

class Logger(Singleton):
    logFile = None

    def __init__(self, path):
        if self.logFile is None:
            self.logFile = open(path, mode='w')
    
    def writeLog(self, logRecord):
        now = str(datetime.datetime.now())
        record = '%s: %s\n' % (now,logRecord)
        self.logFile.write(record)

    def closeLog(self):
        self.logFile.close()
        self.logFile = None