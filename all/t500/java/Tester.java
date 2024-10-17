package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testDecimalScore() {
        // Test a simple decimal score.
        assertEquals(2.5, convertScoreToDecimal("2.5"), 0.001);
    }

    @Test
    public void testFractionScore() {
        // Test a fraction score.
        assertEquals(2.5, convertScoreToDecimal("10/4"), 0.001);
    }

    @Test
    public void testIntegerScore() {
        // Test an integer score represented as a string.
        assertEquals(5.0, convertScoreToDecimal("5"), 0.001);
    }

    @Test
    public void testIntegerDivideScore() {
        // Test an integer division score.
        assertEquals(4.0, convertScoreToDecimal("12/3"), 0.001);
    }

    // Utility method to convert the score to decimal
    private Double convertScoreToDecimal(String scoreStr) {
        try {
            // Check if the score is a fraction
            if (scoreStr.contains("/")) {
                String[] parts = scoreStr.split("/");
                if (parts.length == 2) {
                    double numerator = Double.parseDouble(parts[0]);
                    double denominator = Double.parseDouble(parts[1]);
                    return numerator / denominator;
                } else {
                    throw new IllegalArgumentException("Invalid fraction format");
                }
            } else {
                // Otherwise, treat it as a decimal
                return Double.parseDouble(scoreStr);
            }

        } catch (NumberFormatException | ArithmeticException e) {
            System.out.println("Error converting '" + scoreStr + "' to decimal: " + e.getMessage());
            return null;
        }
    }
}