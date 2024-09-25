import os
import sys
import logging

from dotenv import load_dotenv


class StreamToLogger:
    """
    Fake file-like stream object that redirects writes to a logger instance.

    Generated with ChatGPT.
    """

    def __init__(self, logger_name, log_level):
        self.logger = logging.getLogger(logger_name)
        self.log_level = log_level

    def write(self, buffer):
        for line in buffer.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass