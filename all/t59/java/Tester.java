package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;

import java.math.BigInteger;

import static org.real.temp.Answer.*;

/**
 * Test class for the probabilityRedBalls method.
 */
public class Tester {

    /**
     * Tests the case where all balls are red.
     */
    @Test
    public void testAllRed() {
        assertEquals(1.0, probabilityRedBalls(5, 5, 0), 0.0);
    }

    /**
     * Tests the case where no red balls are available.
     */
    @Test
    public void testNoRed() {
        assertEquals(0.0, probabilityRedBalls(1, 0, 5), 0.0);
    }

    /**
     * Tests a typical scenario.
     */
    @Test
    public void testTypicalCase() {
        double expected = comb(10, 2).doubleValue() / comb(15, 2).doubleValue();
        assertEquals(expected, probabilityRedBalls(2, 10, 5), 0.0001);
    }

    /**
     * Tests the case where more balls are requested than available.
     */
    @Test
    public void testImpossibleCase() {
        assertEquals(0.0, probabilityRedBalls(6, 5, 4), 0.0);
    }

    /**
     * Tests the case with a higher number of combinations.
     */
    @Test
    public void testHighCombinations() {
        double expected = comb(20, 3).doubleValue() / comb(50, 3).doubleValue();
        assertEquals(expected, probabilityRedBalls(3, 20, 30), 0.0001);
    }

    /**
     * Calculates the number of combinations (n choose k).
     *
     * @param n The total number of items.
     * @param k The number of items to choose.
     * @return The number of combinations.
     */
    private BigInteger comb(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for (int i = 0; i < k; i++) {
            result = result.multiply(BigInteger.valueOf(n - i))
                    .divide(BigInteger.valueOf(i + 1));
        }
        return result;
    }
}
