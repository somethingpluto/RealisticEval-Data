package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the cleanPattern method.
 */
public class Tester {

    private String pattern;

    @Before
    public void setUp() {
        // Set up a common regex pattern for testing
        pattern = "(\\d+\\.?\\d*) kg";  // Regex pattern to match weight in kg
    }

    @Test
    public void testValidIntegerWeight() {
        // Test case for valid integer weight
        String inputString = "The weight is 25 kg";
        Object result = cleanPattern(inputString, pattern);
        assertEquals(25.0f, result);
    }

    @Test
    public void testValidFloatWeight() {
        // Test case for valid float weight
        String inputString = "Weight measured at 15.75 kg";
        Object result = cleanPattern(inputString, pattern);
        assertEquals(15.75f, result);
    }

    @Test
    public void testNoWeightFound() {
        // Test case where no weight is present
        String inputString = "No weight provided.";
        Object result = cleanPattern(inputString, pattern);
        assertEquals("", result);
    }

    @Test
    public void testInvalidFloatConversion() {
        // Test case for non-numeric weight
        String inputString = "The weight is thirty kg";
        Object result = cleanPattern(inputString, pattern);
        assertEquals("", result);
    }

    @Test
    public void testWeightWithExtraText() {
        // Test case for weight with additional text
        String inputString = "The total weight is 45.3 kg as per the last measurement.";
        Object result = cleanPattern(inputString, pattern);
        assertEquals(45.3f, result);
    }
}