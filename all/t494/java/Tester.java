package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.HashMap;
import java.util.Map;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testValidStrings() {
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
        Map<String, Object> inputDict = new HashMap<>();
        inputDict.put("key1", null);
        inputDict.put("key3", "valid string");

        Map<String, Object> expectedOutput = new HashMap<>();
        expectedOutput.put("key3", "valid string");

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }

    @Test
    public void testWhitespaceStrings() {
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
        Map<String, Object> inputDict = new HashMap<>();
        Map<String, Object> expectedOutput = new HashMap<>();

        assertEquals(expectedOutput, cleanDictionary(inputDict));
    }
}