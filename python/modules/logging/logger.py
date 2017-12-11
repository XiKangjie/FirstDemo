# As an example scenario, an application want to send all log messages to a log file,
# all log messages of error or higher to stdout.

import logging

# create logger
logger = logging.getLogger("LoggerDemo")
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
fh = logging.FileHandler("all.log")
fh.setLevel(logging.DEBUG)

# create console handler and set level to error
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s")

# add formatter to ch
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add fh and ch to logger
logger.addHandler(fh)
logger.addHandler(ch)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")