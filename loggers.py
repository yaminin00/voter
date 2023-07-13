import os
import logging
from pytz import timezone
from datetime import datetime

os.makedirs('./log', exist_ok=True)

def init_logger(name):
    log='./log/'
    logger = logging.getLogger(name)
    logger_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_handler = logging.FileHandler(f'{log+str(name)}.log')
    log_handler.setLevel(logging.INFO)
    # log_handler.setLevel(logging.ERROR)
    # * old logger format
    log_handler.setFormatter(logging.Formatter(logger_format))
    logger.addHandler(log_handler)
    stream_h = logging.StreamHandler()
    stream_h.setLevel(logging.DEBUG)
    stream_h.setFormatter(logging.Formatter(logger_format))
    logger.addHandler(stream_h)
    logger.setLevel(logging.DEBUG)
    return logger


def get_logger(name):
    return logging.getLogger(name)