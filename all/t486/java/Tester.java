package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

/**
 * Test class for the Calculator.
 */
public class Tester {

    private Calculator calculator;

    @Before
    public void setUp() {
        // Create an instance of Calculator before each test.
        calculator = new Calculator();
    }

    @Test
    public void testAdd() {
        // Test the addition method.
        double result = calculator.add(10, 5);
        assertEquals(15.0, result, 0.0);
    }

    @Test
    public void testSubtract() {
        // Test the subtraction method.
        double result = calculator.subtract(10, 5);
        assertEquals(5.0, result, 0.0);
    }

    @Test
    public void testMultiply() {
        // Test the multiplication method.
        double result = calculator.multiply(10, 5);
        assertEquals(50.0, result, 0.0);
    }

    @Test
    public void testDivide() {
        // Test the division method.
        double result = calculator.divide(10, 5);
        assertEquals(2.0, result, 0.0);
    }

    @Test
    public void testDivideByZero() {
        // Test division by zero raises IllegalArgumentException.
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(10, 0));
    }
}