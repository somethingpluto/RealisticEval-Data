package org.real.temp;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testAverageOfPositiveIntegers() {
        double result = getArrayAverage(new int[]{1, 2, 3, 4, 5});
        assertEquals(3, result, 0.0001); // (1 + 2 + 3 + 4 + 5) / 5 = 3
    }

    @Test
    public void testAverageWithNegativeNumbers() {
        double result = getArrayAverage(new int[]{-1, -2, -3, -4, -5});
        assertEquals(-3, result, 0.0001); // (-1 + -2 + -3 + -4 + -5) / 5 = -3
    }

    @Test
    public void testAverageWithMixedNumbers() {
        double result = getArrayAverage(new int[]{1, -1, 2, -2, 3, -3});
        assertEquals(0, result, 0.0001); // (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0
    }

    @Test
    public void testEmptyArray() {
        double result = getArrayAverage(new int[]{});
        assertTrue(Double.isNaN(result)); // Division by zero, expected result is NaN
    }

    @Test
    public void testSingleElementArray() {
        double result = getArrayAverage(new int[]{7});
        assertEquals(7, result, 0.0001); // The average of [7] is 7
    }
}