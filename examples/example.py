import sys

import logging4

logger = logging4.Logger(name="MyLogger")

formatter = '{time} - {name} - {level_name} - {msg}'

# add/del channel
logger.add_channel(filename='log.txt', level=logging4.WARNING)
logger.add_channel(filename=sys.stdout, level=logging4.ERROR, formatter=formatter)
logger.add_channel(filename='log2.txt', level=logging4.INFO)
logger.del_channel(filename='log2.txt')

# use logger
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

