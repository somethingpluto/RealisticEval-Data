package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.real.temp.Answer.*;

/**
 * Test cases for the wordFilterCounter method.
 */
public class Tester {

    /**
     * Test case 1: Verifies the correct count of specified words in the given text.
     */
    @Test
    public void testCase1() {
        String text = "go to the school.go to the park.";
        List<String> filterWords = Arrays.asList("go", "to", "the", "school", "park", "play");
        Map<String, Integer> expectedOutput = new HashMap<>();
        expectedOutput.put("go", 2);
        expectedOutput.put("to", 2);
        expectedOutput.put("the", 2);
        expectedOutput.put("school", 1);
        expectedOutput.put("park", 1);
        expectedOutput.put("play", 0);

        Map<String, Integer> actualOutput = wordFilterCounter(text, filterWords);
        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case 2: Verifies the correct count of specified words in the given text.
     */
    @Test
    public void testCase2() {
        String text = "This is a completely different sentence.";
        List<String> filterWords = Arrays.asList("I'll", "go", "to", "the", "school", "park", "play");
        Map<String, Integer> expectedOutput = new HashMap<>();
        expectedOutput.put("I'll", 0);
        expectedOutput.put("go", 0);
        expectedOutput.put("to", 0);
        expectedOutput.put("the", 0);
        expectedOutput.put("school", 0);
        expectedOutput.put("park", 0);
        expectedOutput.put("play", 0);

        Map<String, Integer> actualOutput = wordFilterCounter(text, filterWords);
        assertEquals(expectedOutput, actualOutput);
    }

    /**
     * Test case 3: Verifies the correct count of specified words in the given text.
     */
    @Test
    public void testCase3() {
        String text = "I will not go to the school's park.";
        List<String> filterWords = Arrays.asList("I", "will", "not", "go", "to", "the", "school's", "park");
        Map<String, Integer> expectedOutput = new HashMap<>();
        expectedOutput.put("I", 1);
        expectedOutput.put("will", 1);
        expectedOutput.put("not", 1);
        expectedOutput.put("go", 1);
        expectedOutput.put("to", 1);
        expectedOutput.put("the", 1);
        expectedOutput.put("school's", 1);
        expectedOutput.put("park", 1);

        Map<String, Integer> actualOutput = wordFilterCounter(text, filterWords);
        assertEquals(expectedOutput, actualOutput);
    }
}