package org.real.temp;

import java.util.logging.*;

public class Answer {
    private Logger logger;

    public Answer(String name, Level level) {
        // Initialize the logger
        this.logger = Logger.getLogger(name);
        this.logger.setLevel(level);

        // Create a handler for the console
        Handler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(level);

        // Create a formatter
        Formatter formatter = new CustomFormatter();

        // Set the formatter to the handler
        consoleHandler.setFormatter(formatter);

        // Add the handler to the logger
        this.logger.addHandler(consoleHandler);
    }

    public void log(Level level, String message) {
        switch (level) {
            case SEVERE:
                logger.severe(message);
                break;
            case WARNING:
                logger.warning(message);
                break;
            case INFO:
                logger.info(message);
                break;
            case CONFIG:
                logger.config(message);
                break;
            case FINE:
            case FINER:
            case FINEST:
                logger.fine(message);
                break;
            default:
                logger.info(message); // Default to info if level is not recognized
        }
    }

    private static class CustomFormatter extends Formatter {
        @Override
        public String format(LogRecord record) {
            return String.format("%1$tF %1$tT - %2$s - %3$s:%4$d - %5$s %n",
                    record.getMillis(),
                    record.getLevel(),
                    record.getSourceFileName(),
                    record.getSourceLineNumber(),
                    record.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example usage
        Answer answer = new Answer("ExampleLogger", Level.ALL);
        answer.log(Level.INFO, "This is an info message.");
        answer.log(Level.SEVERE, "This is a severe message.");
    }
}