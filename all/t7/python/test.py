import logging
import unittest
from unittest.mock import patch
from io import StringIO


class TestLogger(unittest.TestCase):

    def setUp(self):
        """Set up a Logger instance for testing."""
        self.logger_name = "TestLogger"
        self.logger = Logger(self.logger_name)

    def test_initialization(self):
        """Test that the logger is initialized with the correct name and level."""
        self.assertEqual(self.logger.logger.name, self.logger_name)
        self.assertEqual(self.logger.logger.level, logging.DEBUG)

    def test_default_logging_level(self):
        """Test that the logger defaults to DEBUG level if not specified."""
        logger_default = Logger("DefaultLogger")
        self.assertEqual(logger_default.logger.level, logging.DEBUG)

    def test_console_handler_added(self):
        """Test that the console handler is added to the logger."""
        handlers = self.logger.logger.handlers
        self.assertGreater(len(handlers), 0)
        self.assertIsInstance(handlers[0], logging.StreamHandler)

