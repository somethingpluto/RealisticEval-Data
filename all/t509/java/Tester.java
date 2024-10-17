package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for modular exponentiation.
 */
public class Tester {

    /**
     * Test with base = 2, exponent = 10, modulus = 1000.
     */
    @Test
    public void testCase1() {
        assertEquals("Test with base = 2, exponent = 10, modulus = 1000", 24, modExp(2, 10, 1000));
    }

    /**
     * Test with base = 3, exponent = 7, modulus = 50.
     */
    @Test
    public void testCase2() {
        assertEquals("Test with base = 3, exponent = 7, modulus = 50", 37, modExp(3, 7, 50));
    }

    /**
     * Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1).
     */
    @Test
    public void testCase3() {
        assertEquals("Test with base = 5, exponent = 0, modulus = 13", 1, modExp(5, 0, 13));
    }

    /**
     * Test with base = 7, exponent = 5, modulus = 20.
     */
    @Test
    public void testCase4() {
        assertEquals("Test with base = 7, exponent = 5, modulus = 20", 7, modExp(7, 5, 20));
    }

    /**
     * Test with base = 10, exponent = 5, modulus = 6.
     */
    @Test
    public void testCase5() {
        assertEquals("Test with base = 10, exponent = 5, modulus = 6", 4, modExp(10, 5, 6));
    }

    /**
     * Performs modular exponentiation: (base^exponent) % modulus efficiently.
     *
     * @param base     The base value.
     * @param exponent The exponent value (should be non-negative).
     * @param modulus  The modulus value (should be positive).
     * @return The result of (base^exponent) % modulus.
     * @throws IllegalArgumentException If modulus is less than or equal to zero.
     */
    private static int modExp(int base, int exponent, int modulus) {
        if (modulus <= 0) {
            throw new IllegalArgumentException("Modulus must be a positive integer.");
        }

        int result = 1;
        base = base % modulus;  // Ensure base is within the modulus

        while (exponent > 0) {
            // If exponent is odd, multiply the base with the result
            if (exponent % 2 == 1) {
                result = (result * base) % modulus;
            }

            // Right shift the exponent by 1 (equivalent to exponent //= 2)
            exponent >>= 1;
            // Square the base
            base = (base * base) % modulus;
        }

        return result;
    }
}