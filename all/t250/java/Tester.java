package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Tester {

    @Test
    public void testInvertDictionary() {
        // Test case 1
        Map<String, Integer> input1 = new HashMap<>();
        input1.put("a", 1);
        input1.put("b", 2);
        input1.put("c", 3);

        Map<Integer, List<String>> expectedOutput1 = new HashMap<>();
        expectedOutput1.put(1, Arrays.asList("a"));
        expectedOutput1.put(2, Arrays.asList("b"));
        expectedOutput1.put(3, Arrays.asList("c"));

        assertEquals(expectedOutput1, DictionaryUtils.invertDictionary(input1));

        // Test case 2
        Map<String, String> input2 = new HashMap<>();
        input2.put("apple", "fruit");
        input2.put("banana", "fruit");
        input2.put("carrot", "vegetable");

        Map<String, List<String>> expectedOutput2 = new HashMap<>();
        expectedOutput2.put("fruit", Arrays.asList("apple", "banana"));
        expectedOutput2.put("vegetable", Arrays.asList("carrot"));

        assertEquals(expectedOutput2, DictionaryUtils.invertDictionary(input2));
    }

    @Test
    public void testInvertDictionaryWithDuplicateValues() {
        // Test case with duplicate values
        Map<String, String> input3 = new HashMap<>();
        input3.put("one", "1");
        input3.put("two", "2");
        input3.put("three", "1");

        Map<String, List<String>> expectedOutput3 = new HashMap<>();
        expectedOutput3.put("1", Arrays.asList("one", "three"));
        expectedOutput3.put("2", Arrays.asList("two"));

        assertEquals(expectedOutput3, DictionaryUtils.invertDictionary(input3));
    }
}