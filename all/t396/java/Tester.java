package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the lengthOfLIS method.
 */
public class Tester {

    /**
     * Tests the function with an empty list.
     */
    @Test
    public void testEmptyList() {
        // Test the function with an empty list
        assertEquals(0, lengthOfLIS(new int[]{}));
    }

    /**
     * Tests the function with a list containing only one element.
     */
    @Test
    public void testSingleElement() {
        // Test with a list containing only one element
        assertEquals(1, lengthOfLIS(new int[]{7}));
    }

    /**
     * Tests the function with a list where the elements are strictly increasing.
     */
    @Test
    public void testIncreasingSequence() {
        // Test with a list where the elements are strictly increasing
        assertEquals(5, lengthOfLIS(new int[]{1, 2, 3, 4, 5}));
    }

    /**
     * Tests the function with a list where the elements are strictly decreasing.
     */
    @Test
    public void testDecreasingSequence() {
        // Test with a list where the elements are strictly decreasing
        assertEquals(1, lengthOfLIS(new int[]{5, 4, 3, 2, 1}));
    }

    /**
     * Tests the function with a complex sequence with a mix of increasing and decreasing elements.
     */
    @Test
    public void testComplexSequence() {
        // Test with a complex sequence with a mix of increasing and decreasing elements
        assertEquals(4, lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
    }

    /**
     * Tests the function with all elements in the list being equal.
     */
    @Test
    public void testAllEqualElements() {
        // Test with all elements in the list being equal
        assertEquals(1, lengthOfLIS(new int[]{2, 2, 2, 2}));
    }

    /**
     * Tests the function with a mix of negative and positive numbers.
     */
    @Test
    public void testWithNegativeNumbers() {
        // Test with a mix of negative and positive numbers
        assertEquals(4, lengthOfLIS(new int[]{-1, -2, -3, 0, 1, 2}));
    }
}