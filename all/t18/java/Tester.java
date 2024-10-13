package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test cases for the floatToRGB method.
 */
public class Tester {

    /**
     * Tests that a value at the lower boundary (0.0) returns pure red.
     */
    @Test
    public void testPureRed() {
        int[] result = floatToRGB(0.0f);
        assertArrayEquals(new int[]{255, 0, 0}, result);
    }

    /**
     * Tests that a value at the upper boundary (1.0) returns pure green.
     */
    @Test
    public void testPureGreen() {
        int[] result = floatToRGB(1.0f);
        assertArrayEquals(new int[]{0, 255, 0}, result);
    }

    /**
     * Tests that a value at 0.5 returns an equal mix of red and green, resulting in yellow.
     */
    @Test
    public void testMidpoint() {
        int[] result = floatToRGB(0.5f);
        assertArrayEquals(new int[]{127, 127, 0}, result);
    }

    /**
     * Tests that a value at 0.25 returns more red than green.
     */
    @Test
    public void testQuarterPoint() {
        int[] result = floatToRGB(0.25f);
        assertArrayEquals(new int[]{191, 63, 0}, result);
    }

    /**
     * Tests that a value outside the range [0, 1] raises an IllegalArgumentException.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testInvalidValue() {
        floatToRGB(1.5f);
    }
}