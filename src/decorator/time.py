from time import time
from functools import wraps

from src.decorator.logging import create_logger

def elapsed_time(function):
    @wraps(function)
    def wrapper(*args, **kwds):
        logger = create_logger()
        start = time()
        result = function(*args, **kwds)
        elapsed = time() - start
        logger.info("%s took %f seconds to finish" % (function.__name__, elapsed))
        return result
    return wrapper