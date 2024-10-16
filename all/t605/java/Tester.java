package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

/**
 * Test class for BMI calculations.
 */
public class Tester {

    // Test case for valid inputs with expected BMI value
    @Test
    public void testValidBMICalculations() {
        // Normal weight
        assertEquals(22.86, Answer.calculateBMI(70, 1.75), 0.01); // 70 kg, 1.75 m

        // Underweight
        assertEquals(16.33, Answer.calculateBMI(50, 1.75), 0.01); // 50 kg, 1.75 m

        // Overweight
        assertEquals(26.12, Answer.calculateBMI(80, 1.75), 0.01); // 80 kg, 1.75 m

        // Obesity
        assertEquals(32.65, Answer.calculateBMI(100, 1.75), 0.01); // 100 kg, 1.75 m
    }

    // Test case for invalid inputs
    @Test
    public void testInvalidBMICalculations() {
        // Negative weight
        assertThrows(IllegalArgumentException.class, () -> {
            Answer.calculateBMI(-70, 1.75);
        });

        // Zero height
        assertThrows(IllegalArgumentException.class, () -> {
            Answer.calculateBMI(70, 0);
        });

        // Negative height
        assertThrows(IllegalArgumentException.class, () -> {
            Answer.calculateBMI(70, -1.75);
        });
    }
}