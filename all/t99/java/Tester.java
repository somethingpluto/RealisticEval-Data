package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testSumNormalArray() {
        assertEquals(15, sum(new int[]{1, 2, 3, 4, 5}));
    }

    @Test
    public void testSumNegativeArray() {
        assertEquals(-15, sum(new int[]{-1, -2, -3, -4, -5}));
    }

    @Test
    public void testSumEmptyArray() {
        assertEquals(0, sum(new int[]{}));
    }

    @Test
    public void testSumMixedArray() {
        assertEquals(15, sum(new int[]{10, -10, 5, -5, 15}));
    }

    @Test
    public void testSumFloatingPointArray() {
        assertEquals(7.5, sum(new double[]{1.5, 2.5, 3.5}), 0.001);
    }
}