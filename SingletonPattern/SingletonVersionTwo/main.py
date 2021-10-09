from LoggerBase import Logger

logger = Logger('/SingletonPattern/SingletonVersionTwo/my.log')
logger.writeLog("logging with the classic singleton pattern")
logger2 = Logger('ignored because of singleton')
logger2.writeLog('Another log entry')

logger.closeLog()

with open ('my.log', 'r') as f:
    for line in f:
        print(line, end='')