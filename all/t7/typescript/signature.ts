/**
 * A class representing a logger.
 */
class Logger {
    private logger: log4js.Logger;
  
    /**
     * Initializes a new logger instance.
     *
     * @param name - Name of the logger, typically __name__ to reference the module name.
     * @param level - Logging level, default is DEBUG.
     */
    constructor(name: string, level: log4js.Level = 'debug') {
    }
  
    /**
     * Logs a message with the given level.
     *
     * @param level - Logging level for the message (e.g., 'debug', 'info').
     * @param message - Log message.
     */
    public log(level: log4js.Level, message: string): void {
    }
  }