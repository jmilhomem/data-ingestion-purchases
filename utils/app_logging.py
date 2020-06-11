"""Logging module."""
import logging as log


def define_log():
    """Define the log."""
    log.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=log.INFO,
                    filename='logs/logs.log')

    logger = log.getLogger('quotes_app')

    return logger
