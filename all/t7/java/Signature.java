public class Logger {
    private static final Logger logger = Logger.getLogger(Logger.class.getName());

    /**
     * Initializes a new logger instance.
     *
     * @param name Name of the logger, typically the name of the class or package.
     * @param level Logging level, default is INFO.
     */
    public Logger(String name, Level level) {}

    /**
     * Logs a message with the given level.
     *
     * @param level Logging level for the message (e.g., Level.INFO).
     * @param message Log message.
     */
    public void log(Level level, String message) {}
}