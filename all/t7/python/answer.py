import logging


class Logger:
    def __init__(self, name, level=logging.DEBUG):
        """
        Initializes a new logger instance.

        :param name: Name of the logger, typically __name__ to reference the module name.
        :param level: Logging level, default is DEBUG.
        """
        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

        # Create console handler and set level and formatter
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)

        # Add handler to the logger
        self.logger.addHandler(console_handler)

    def log(self, level, message):
        """
        Logs a message with the given level.

        :param level: Logging level for the message (e.g., logging.INFO).
        :param message: Log message.
        """
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
