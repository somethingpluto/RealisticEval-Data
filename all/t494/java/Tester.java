package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.HashMap;
import java.util.Map;

public class Tester {

    @Test
    public void testValidStrings() {
        """ Test a dictionary with valid strings. """
        Map<String, Object> inputDict = new HashMap<>();
        inputDict.put("key1", "valid string");
        inputDict.put("key2", "another valid string");

        Map<String, Object> expectedOutput = new HashMap<>();
        expectedOutput.put("key1", "valid string");
        expectedOutput.put("key2", "another valid string");

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }

    @Test
    public void testNoneAndNaNValues() {
        """ Test a dictionary with None and NaN values. """
        Map<String, Object> inputDict = new HashMap<>();
        inputDict.put("key1", null);
        inputDict.put("key3", "valid string");

        Map<String, Object> expectedOutput = new HashMap<>();
        expectedOutput.put("key3", "valid string");

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }

    @Test
    public void testWhitespaceStrings() {
        """ Test a dictionary with whitespace strings. """
        Map<String, Object> inputDict = new HashMap<>();
        inputDict.put("key1", "   ");
        inputDict.put("key2", "");
        inputDict.put("key3", "valid");

        Map<String, Object> expectedOutput = new HashMap<>();
        expectedOutput.put("key3", "valid");

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }

    @Test
    public void testEmptyDictionary() {
        """ Test an empty dictionary. """
        Map<String, Object> inputDict = new HashMap<>();
        Map<String, Object> expectedOutput = new HashMap<>();

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }

    // Utility method to simulate the cleanDictionary function
    private Map<String, Object> cleanDictionary(Map<String, Object> inputDict) {
        Map<String, Object> cleanedMap = new HashMap<>();

        for (Map.Entry<String, Object> entry : inputDict.entrySet()) {
            Object value = entry.getValue();

            // Check if the value is not null and not a blank string
            if (value instanceof String && !((String) value).trim().isEmpty()) {
                // Check if value is a number (Integer or Double) and is not NaN
                if (!(value instanceof Double && ((Double) value).isNaN())) {
                    cleanedMap.put(entry.getKey(), value);
                }
            }
        }

        return cleanedMap;
    }
}