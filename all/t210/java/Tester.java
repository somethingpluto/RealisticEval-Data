package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    // Test Case 1: Fibonacci of 0
    @Test
    public void testFibonacciZero() {
        assertEquals(0, fibonacciRecursive(0));
    }

    // Test Case 2: Fibonacci of 1
    @Test
    public void testFibonacciOne() {
        assertEquals(1, fibonacciRecursive(1));
    }

    // Test Case 3: Fibonacci of 5
    @Test
    public void testFibonacciFive() {
        assertEquals(5, fibonacciRecursive(5));
    }

    // Test Case 4: Fibonacci of 10
    @Test
    public void testFibonacciTen() {
        assertEquals(55, fibonacciRecursive(10));
    }

    // Test Case 5: Fibonacci of 20
    @Test
    public void testFibonacciTwenty() {
        assertEquals(6765, fibonacciRecursive(20));
    }
}