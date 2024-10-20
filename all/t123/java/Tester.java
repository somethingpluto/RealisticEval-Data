package org.real.temp;

import static org.junit.Assert.*;

import org.junit.Test;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testSimpleScaling() {
        double[] result = scaleToRange(new double[]{1, 2, 3, 4, 5}, 1, 5, 10, 50);
        assertArrayEquals(new double[]{10, 20, 30, 40, 50}, result, 0.001);
    }

    @Test
    public void testScalingWithNegativeInputRange() {
        double[] result = scaleToRange(new double[]{-5, 0, 5}, -5, 5, 0, 100);
        assertArrayEquals(new double[]{0, 50, 100}, result, 0.001);
    }

    @Test
    public void testScalingWithNegativeOutputRange() {
        double[] result = scaleToRange(new double[]{0, 50, 100}, 0, 100, -100, 100);
        assertArrayEquals(new double[]{-100, 0, 100}, result, 0.001);
    }

    @Test
    public void testInputArrayContainingSameValue() {
        double[] result = scaleToRange(new double[]{2, 2, 2}, 1, 3, 0, 10);
        assertArrayEquals(new double[]{5, 5, 5}, result, 0.001);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInputValueOutOfRangeShouldThrowError() {
        scaleToRange(new double[]{1, 2, 3, 6}, 1, 5, 0, 10);
    }
}