package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

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

    // Method to be tested
    private Object cleanPattern(Object x, String pattern) {
        // Convert input to string
        String input = x.toString();

        // Compile the pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(input);

        if (matcher.find()) {
            // Extract the weight value from the first matching group
            String weight = matcher.group(1);  // Can also use matcher.group(3) if needed

            try {
                // Convert the weight to a float and return it
                float weightValue = Float.parseFloat(weight);
                return weightValue;
            } catch (NumberFormatException e) {
                // Handle cases where conversion to float fails
                System.out.println("Warning: Unable to convert '" + weight + "' to float.");
                return "";
            }
        } else {
            return "";  // Return empty string if no match is found
        }
    }
}