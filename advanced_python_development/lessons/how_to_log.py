import logging

'''
logging is used to print things out in a variety of ways
it has a variety of levels of logging:
DEBUG - does not show up by default. Only use while developing
INFO - does not show up by default
WARNING
ERROR
CRITICAL

Create a new logger for each module
'''

# Configure logger level, file to receive logs and format the logger message
# log files DO NOT GET OVERWRITTEN. They get appended to
awesome_logging_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(format=awesome_logging_format, level=logging.INFO, filename='logs.txt')    
logger = logging.getLogger('test_logger')

logger.info('This is information')
logger.warning('This is a warning')

# Write log to file