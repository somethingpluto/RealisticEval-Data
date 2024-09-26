import logging
import unittest
from unittest.mock import patch


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger_name = 'test_logger'
        self.logger = Logger(self.logger_name)

    @patch('logging.Logger.debug')
    def test_debug_logging(self, mock_debug):
        message = "This is a debug message"
        self.logger.log(logging.DEBUG, message)
        mock_debug.assert_called_once_with(message)

    @patch('logging.Logger.info')
    def test_info_logging(self, mock_info):
        message = "This is an info message"
        self.logger.log(logging.INFO, message)
        mock_info.assert_called_once_with(message)

    @patch('logging.Logger.warning')
    def test_warning_logging(self, mock_warning):
        message = "This is a warning message"
        self.logger.log(logging.WARNING, message)
        mock_warning.assert_called_once_with(message)

    @patch('logging.Logger.error')
    def test_error_logging(self, mock_error):
        message = "This is an error message"
        self.logger.log(logging.ERROR, message)
        mock_error.assert_called_once_with(message)

    @patch('logging.Logger.critical')
    def test_critical_logging(self, mock_critical):
        message = "This is a critical message"
        self.logger.log(logging.CRITICAL, message)
        mock_critical.assert_called_once_with(message)
