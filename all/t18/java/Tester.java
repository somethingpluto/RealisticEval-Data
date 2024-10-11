package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class TestFloatToRGB {

    @Test
    public void testPureRed() {
        // Value at the lower boundary (0.0) should return pure red
        int[] result = floatToRGB(0.0);
        assertArrayEquals(new int[]{255, 0, 0}, result);
    }

    @Test
    public void testPureGreen() {
        // Value at the upper boundary (1.0) should return pure green
        int[] result = floatToRGB(1.0);
        assertArrayEquals(new int[]{0, 255, 0}, result);
    }

    @Test
    public void testMidpoint() {
        // Value at 0.5 should return an equal mix of red and green, resulting in yellow
        int[] result = floatToRGB(0.5);
        assertArrayEquals(new int[]{127, 127, 0}, result);
    }

    @Test
    public void testQuarterPoint() {
        // Value at 0.25 should return more red than green
        int[] result = floatToRGB(0.25);
        assertArrayEquals(new int[]{191, 63, 0}, result);
    }

    @Test
    public void testInvalidValue() {
        // Value outside the range [0, 1] should raise a ValueError
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            floatToRGB(1.5);
        });
        assertEquals("Value must be between 0.0 and 1.0", exception.getMessage());
    }
}
