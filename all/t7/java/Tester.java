package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.util.logging.ConsoleHandler;
import java.util.logging.SimpleFormatter;

/**
 * Test class for the Logger functionality.
 */
public class Tester {

    private Logger logger;
    private String loggerName = "TestLogger";

    /**
     * Set up a Logger instance for testing.
     */
    @Before
    public void setUp() {
        logger = Logger.getLogger(loggerName);
        logger.setLevel(Level.ALL);

        // Create a console handler and set its level
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);

        // Create a formatter and set it to the handler
        SimpleFormatter formatter = new SimpleFormatter();
        consoleHandler.setFormatter(formatter);

        // Add the handler to the logger
        logger.addHandler(consoleHandler);
    }

    /**
     * Test that the logger is initialized with the correct name and level.
     */
    @Test
    public void testInitialization() {
        assertEquals(logger.getName(), loggerName);
        assertEquals(logger.getLevel(), Level.ALL);
    }

    /**
     * Test that the logger defaults to ALL level if not specified.
     */
    @Test
    public void testDefaultLoggingLevel() {
        Logger defaultLogger = Logger.getLogger("DefaultLogger");
        assertEquals(defaultLogger.getLevel(), Level.ALL);
    }

    /**
     * Test that the console handler is added to the logger.
     */
    @Test
    public void testConsoleHandlerAdded() {
        assertNotNull(logger.getHandlers());
        assertTrue(logger.getHandlers().length > 0);
        assertTrue(logger.getHandlers()[0] instanceof ConsoleHandler);
    }
}