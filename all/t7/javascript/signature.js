class Logger {
    /**
     * Initializes a new logger instance.
     *
     * @param {string} name - Name of the logger, typically __filename to reference the file name.
     * @param {number} [level=debug] - Logging level, default is debug.
     */
    constructor(name, level = 'debug') {}

    /**
     * Logs a message with the given level.
     *
     * @param {string} level - Logging level for the message (e.g., 'info').
     * @param {string} message - Log message.
     */
    log(level, message) {}
}