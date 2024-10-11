const { createLogger, format, transports } = require('winston');

class Logger {
  constructor(name, level = 'debug') {
    /**
     * Initializes a new logger instance.
     *
     * @param {string} name - Name of the logger, typically __name__ to reference the module name.
     * @param {string} level - Logging level, default is debug.
     */

    this.logger = createLogger({
      level,
      format: format.json(),
      transports: [
        new transports.Console()
      ]
    });
  }

  log(level, message) {
    /**
     * Logs a message with the given level.
     *
     * @param {string} level - Logging level for the message (e.g., info).
     * @param {string} message - Log message.
     */
    
    this.logger.log({ level, message });
  }
}