class Logger {
    constructor(name, level = 'DEBUG') {
        /**
         * Initializes a new logger instance.
         *
         * @param {string} name - Name of the logger, typically the module name.
         * @param {string} level - Logging level, default is DEBUG.
         */
        this.name = name;
        this.level = level;
        this.levels = {
            DEBUG: 0,
            INFO: 1,
            WARNING: 2,
            ERROR: 3,
            CRITICAL: 4
        };
    }

    log(level, message) {
        /**
         * Logs a message with the given level.
         *
         * @param {string} level - Logging level for the message (e.g., 'INFO').
         * @param {string} message - Log message.
         */
        if (this.levels[level] >= this.levels[this.level]) {
            const timestamp = new Date().toISOString();
            switch (level) {
                case 'DEBUG':
                    console.debug(`${timestamp} - DEBUG - ${this.name}: ${message}`);
                    break;
                case 'INFO':
                    console.info(`${timestamp} - INFO - ${this.name}: ${message}`);
                    break;
                case 'WARNING':
                    console.warn(`${timestamp} - WARNING - ${this.name}: ${message}`);
                    break;
                case 'ERROR':
                    console.error(`${timestamp} - ERROR - ${this.name}: ${message}`);
                    break;
                case 'CRITICAL':
                    console.error(`${timestamp} - CRITICAL - ${this.name}: ${message}`);
                    break;
                default:
                    console.log(`${timestamp} - ${level} - ${this.name}: ${message}`);
                    break;
            }
        }
    }
}

// Example usage:
const logger = new Logger("MyModule", "DEBUG");
logger.log("INFO", "This is an info message");
logger.log("DEBUG", "This is a debug message");
logger.log("WARNING", "This is a warning message");
logger.log("ERROR", "This is an error message");
logger.log("CRITICAL", "This is a critical message");