const winston = require('winston');

class Logger {
    constructor(name, level = 'debug') {
        /**
         * Initializes a new logger instance.
         *
         * @param {string} name - Name of the logger, typically __filename to reference the module name.
         * @param {string} level - Logging level, default is 'debug'.
         */
        // Create logger
        this.logger = winston.createLogger({
            level: level,
            format: winston.format.combine(
                winston.format.timestamp(),
                winston.format.printf(info => {
                    return `${info.timestamp} - ${info.level.toUpperCase()} - ${info.filename}:${info.line}:${info.message}`;
                })
            ),
            transports: [
                new winston.transports.Console({
                    level: level,
                    format: winston.format.combine(
                        winston.format.colorize(),
                        winston.format.printf(info => {
                            return `${info.timestamp} - ${info.level.toUpperCase()} - ${info.filename}:${info.line}:${info.message}`;
                        })
                    )
                })
            ]
        });

        // Set filename and line number
        this.logger.filename = name;
        this.logger.line = 0; // This will be updated when logging
    }

    log(level, message) {
        /**
         * Logs a message with the given level.
         *
         * @param {string} level - Logging level for the message (e.g., 'debug', 'info').
         * @param {string} message - Log message.
         */
        switch (level) {
            case 'debug':
                this.logger.debug(message);
                break;
            case 'info':
                this.logger.info(message);
                break;
            case 'warn':
                this.logger.warn(message);
                break;
            case 'error':
                this.logger.error(message);
                break;
            case 'critical':
                this.logger.critical(message);
                break;
            default:
                this.logger.log(level, message);
                break;
        }
    }
}