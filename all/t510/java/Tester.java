package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
/**
 * Test class for verifying the correctness of the findPowers method.
 */
public class Tester {

    /**
     * Tests valid numbers with only 2's and 3's as prime factors.
     */
    @Test
    public void testValidCases() {
        assertEquals("[1, 2]", Arrays.toString(findPowers(18)));  // 18 = 2^1 * 3^2
        assertEquals("[3, 0]", Arrays.toString(findPowers(8)));   // 8 = 2^3 * 3^0
        assertEquals("[0, 3]", Arrays.toString(findPowers(27)));  // 27 = 2^0 * 3^3
        assertEquals("[2, 1]", Arrays.toString(findPowers(12)));  // 12 = 2^2 * 3^1
        assertEquals("[0, 0]", Arrays.toString(findPowers(1)));   // 1 = 2^0 * 3^0
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
        assertEquals("[5, 3]", Arrays.toString(findPowers(864)));  // 864 = 2^5 * 3^3
        assertEquals("[0, 6]", Arrays.toString(findPowers(729)));  // 729 = 2^0 * 3^6
    }

    /**
     * Tests edge cases for minimal inputs.
     */
    @Test
    public void testEdgeCases() {
        assertEquals("[1, 0]", Arrays.toString(findPowers(2)));   // 2 = 2^1 * 3^0
        assertEquals("[0, 1]", Arrays.toString(findPowers(3)));   // 3 = 2^0 * 3^1
    }

}