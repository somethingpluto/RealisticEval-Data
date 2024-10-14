package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {
    @Test
    public void testZeroDegrees() {
        // Test conversion of 0 degrees
        assertEquals(0, degreesToRadians(0), 1e-5);
    }

    @Test
    public void testNinetyDegrees() {
        // Test conversion of 90 degrees
        assertEquals(Math.PI / 2, degreesToRadians(90), 1e-5);
    }

    @Test
    public void testOneEightyDegrees() {
        // Test conversion of 180 degrees
        assertEquals(Math.PI, degreesToRadians(180), 1e-5);
    }

    @Test
    public void testTwoSeventyDegrees() {
        // Test conversion of 270 degrees
        assertEquals(3 * Math.PI / 2, degreesToRadians(270), 1e-5);
    }

    @Test
    public void testThreeSixtyDegrees() {
        // Test conversion of 360 degrees
        assertEquals(2 * Math.PI, degreesToRadians(360), 1e-5);
    }

    @Test
    public void testNegativeDegrees() {
        // Test conversion of negative degrees
        assertEquals(-Math.PI / 2, degreesToRadians(-90), 1e-5);
    }

    @Test
    public void testLargeDegrees() {
        // Test conversion of a large angle (720 degrees)
        assertEquals(4 * Math.PI, degreesToRadians(720), 1e-5);
    }
}