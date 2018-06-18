import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=20,
                                               backupCount=3)
my_logger.addHandler(handler)

# log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)

