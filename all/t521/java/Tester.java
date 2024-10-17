package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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

    // Method to be tested
    private Map<String, Integer> wordFilterCounter(String text, List<String> filterWords) {
        // Convert filter words to lowercase for case-insensitive comparison
        Set<String> filterWordsSet = new HashSet<>();
        for (String word : filterWords) {
            filterWordsSet.add(word.toLowerCase());
        }

        // Find all words in the text using a regex pattern
        Pattern pattern = Pattern.compile("\\b\\w+(?:'\\w+)?\\b");
        Matcher matcher = pattern.matcher(text.toLowerCase());
        List<String> words = new ArrayList<>();
        while (matcher.find()) {
            words.add(matcher.group());
        }

        // Count occurrences of filtered words
        Map<String, Integer> wordCounts = new HashMap<>();
        for (String word : words) {
            if (filterWordsSet.contains(word)) {
                wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
            }
        }

        // Create an ordered output based on the original order of filterWords
        Map<String, Integer> orderedOutput = new LinkedHashMap<>();
        for (String word : filterWords) {
            orderedOutput.put(word, wordCounts.getOrDefault(word.toLowerCase(), 0));
        }

        return orderedOutput;
    }
}