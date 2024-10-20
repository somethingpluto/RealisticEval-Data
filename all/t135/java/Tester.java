package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testValidPortNumber_MiddleOfRange() {
        assertTrue(isValidPortNumber(8080));
    }

    @Test
    public void testValidPortNumber_Lowest() {
        assertTrue(isValidPortNumber(1));
    }

    @Test
    public void testValidPortNumber_Highest() {
        assertTrue(isValidPortNumber(65535));
    }

    @Test
    public void testValidPortNumber_BelowRange() {
        assertFalse(isValidPortNumber(0));
    }

    @Test
    public void testValidPortNumber_AboveRange() {
        assertFalse(isValidPortNumber(65536));
    }

    // The method to be tested
    public static boolean isValidPortNumber(int port) {
        return port >= 1 && port <= 65535;
    }
}