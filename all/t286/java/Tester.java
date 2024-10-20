package org.real.temp;

import org.junit.Test;

import java.util.Optional;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testTypicalCase() {
        // Test with a typical input where the largest divisible number should be found.
        assertEquals(Optional.of(50).get(), findLargestDivisible(50));
        assertEquals(Optional.of(45).get(), findLargestDivisible(47));
    }

    @Test
    public void testNoDivisibleFound() {
        // Test a case where no divisible number is found within the range.
        assertTrue(findLargestDivisible(4) ==null);
    }

    @Test
    public void testExactHalfDivisible() {
        // Test when the half of n is exactly divisible by 5.
        assertEquals(Optional.of(10).get(), findLargestDivisible(10));
    }

    @Test
    public void testLargeNumber() {
        // Test with a large number to ensure performance and correctness.
        assertEquals(Optional.of(1000).get(), findLargestDivisible(1000));
    }

    @Test
    public void testLowerBound() {
        // Test the function with the lowest bound that should find a divisible number.
        assertEquals(Optional.of(5).get(), findLargestDivisible(5));
    }
}