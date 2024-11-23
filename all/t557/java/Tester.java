package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for converting radians to degrees.
 */
public class Tester {

    /**
     * Test conversion of 0 radians.
     */
    @Test
    public void testZeroRadians() {
        assertEquals("Conversion of 0 radians", 0, radiansToDegrees(0), 0.00001);
    }

    /**
     * Test conversion of π/2 radians.
     */
    @Test
    public void testPiOverTwoRadians() {
        assertEquals("Conversion of π/2 radians", 90, radiansToDegrees(Math.PI / 2), 0.00001);
    }

    /**
     * Test conversion of π radians.
     */
    @Test
    public void testPiRadians() {
        assertEquals("Conversion of π radians", 180, radiansToDegrees(Math.PI), 0.00001);
    }

    /**
     * Test conversion of 3π/2 radians.
     */
    @Test
    public void testThreePiOverTwoRadians() {
        assertEquals("Conversion of 3π/2 radians", 270, radiansToDegrees(3 * Math.PI / 2), 0.00001);
    }

    /**
     * Test conversion of 2π radians.
     */
    @Test
    public void testTwoPiRadians() {
        assertEquals("Conversion of 2π radians", 360, radiansToDegrees(2 * Math.PI), 0.00001);
    }

    /**
     * Test conversion of -π/2 radians.
     */
    @Test
    public void testNegativePiOverTwoRadians() {
        assertEquals("Conversion of -π/2 radians", -90, radiansToDegrees(-Math.PI / 2), 0.00001);
    }

    /**
     * Test conversion of a large angle (4π radians).
     */
    @Test
    public void testLargeRadians() {
        assertEquals("Conversion of 4π radians", 720, radiansToDegrees(4 * Math.PI), 0.00001);
    }
}