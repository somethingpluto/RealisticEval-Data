package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private Logger logger;

    @BeforeEach
    public void setUp() {
        // Initialize the logger before each test method
        logger = new Logger("TestLogger");
    }

    @Test
    public void testLogInfo() {
        String message = "This is an info message";
        logger.log(Logger.Level.INFO, message);
        // Add assertions here to verify the log message was processed correctly
        // For example, check if the message is stored in a list or logged to a file
    }

    @Test
    public void testLogError() {
        String message = "This is an error message";
        logger.log(Logger.Level.ERROR, message);
        // Add assertions here to verify the log message was processed correctly
    }

    // Define the Logger class with necessary methods and properties
    public static class Logger {
        public enum Level {
            INFO,
            ERROR
        }

        private final String name;

        public Logger(String name) {
            this.name = name;
        }

        public void log(Level level, String message) {
            // Implement the logic to log messages based on the level
            System.out.println("[" + level + "] " + name + ": " + message);
        }
    }
}