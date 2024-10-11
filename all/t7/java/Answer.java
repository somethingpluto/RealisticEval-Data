package org.real.temp;

import java.util.logging.Level;
import java.util.logging.Logger;

public class Answer {
    private static final Logger LOGGER = Logger.getLogger(Answer.class.getName());

    public void log(Level level, String message) {
        LOGGER.log(level, message);
    }