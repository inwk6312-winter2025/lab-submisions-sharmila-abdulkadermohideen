import logging

name = 'John'
logging.error(f'{name} raised an error')

import logging
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)

try:
    c = a / b
except Exception as e:
    logging.exception("Exception occurred")

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')