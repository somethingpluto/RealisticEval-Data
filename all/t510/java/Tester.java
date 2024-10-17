package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for verifying the correctness of the findPowers method.
 */
public class Tester {

    /**
     * Tests valid numbers with only 2's and 3's as prime factors.
     */
    @Test
    public void testValidCases() {
        assertEquals("(1, 2)", Arrays.toString(findPowers(18)));  // 18 = 2^1 * 3^2
        assertEquals("(3, 0)", Arrays.toString(findPowers(8)));   // 8 = 2^3 * 3^0
        assertEquals("(0, 3)", Arrays.toString(findPowers(27)));  // 27 = 2^0 * 3^3
        assertEquals("(2, 1)", Arrays.toString(findPowers(12)));  // 12 = 2^2 * 3^1
        assertEquals("(0, 0)", Arrays.toString(findPowers(1)));   // 1 = 2^0 * 3^0
    }

    /**
     * Tests numbers with prime factors other than 2 and 3.
     */
    @Test
    public void testInvalidCases() {
        assertNull(findPowers(7));    // 7 is a prime factor
        assertNull(findPowers(14));   // 14 = 2^1 * 7^1 (contains 7)
        assertNull(findPowers(10));   // 10 = 2^1 * 5^1 (contains 5)
    }

    /**
     * Tests large numbers that have only 2 and 3 as prime factors.
     */
    @Test
    public void testLargeNumbers() {
        assertEquals("(5, 3)", Arrays.toString(findPowers(864)));  // 864 = 2^5 * 3^3
        assertEquals("(0, 6)", Arrays.toString(findPowers(729)));  // 729 = 2^0 * 3^6
    }

    /**
     * Tests edge cases for minimal inputs.
     */
    @Test
    public void testEdgeCases() {
        assertEquals("(1, 0)", Arrays.toString(findPowers(2)));   // 2 = 2^1 * 3^0
        assertEquals("(0, 1)", Arrays.toString(findPowers(3)));   // 3 = 2^0 * 3^1
    }

    // Utility method to simulate the findPowers method
    private Integer[] findPowers(int num) {
        // Input validation
        if (num <= 0) {
            throw new IllegalArgumentException("Input must be a positive integer greater than zero.");
        }

        int n = 0; // Initialize counter for powers of 2
        int m = 0; // Initialize counter for powers of 3

        // Count the power of 2 in the factorization
        while (num % 2 == 0) {
            n++;
            num /= 2;
        }

        // Count the power of 3 in the factorization
        while (num % 3 == 0) {
            m++;
            num /= 3;
        }

        // If num is reduced to 1, only 2's and 3's were factors
        if (num == 1) {
            return new Integer[]{n, m};
        } else {
            return null; // Return null if there are other prime factors
        }
    }
}