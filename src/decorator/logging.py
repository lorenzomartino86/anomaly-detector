import functools
import logging
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_logger(name="anomaly-detector-logger"):
    """
    creates a logging instance and returns it
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # creating logging file handler
    handler = logging.FileHandler(ROOT_DIR + 'anomaly-detector.log')

    formatting_style = '%(asctime)s - %(name)s - %(thread)d - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatting_style)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def exception(function):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            err = "There was an exception in  "
            err += function.__name__
            logger.exception(err)

            # re-raise the exception
            raise

    return wrapper