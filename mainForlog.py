import logging

'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''
logger = None
def logInit():
    ctrlShow = logging.StreamHandler()
    ctrlShow.setLevel(logging.DEBUG)
    logger = logging.getLogger('TCF')
    logging.basicConfig(filename='log_test.log', level=logging.NOTSET, handlers=ctrlShow)

    print(logger.handlers)

    logger.info('Today is a nice day.')
    logger.debug('Today is a nice day.')
    logger.warning('Today is a nice day.')
    logger.error('Today is a nice day.')



if __name__ == '__main__':
    logInit()
