from LoggerMeta import Logger

logger = Logger('my.log')
logger.writeLog('Meta class logging')
logger2 = Logger('doesntmatter')
logger2.writeLog('öeöeöeöe')

logger.closeLog()

with open('my.log', mode='r') as f:
    for line in f:
        print(line, end='')