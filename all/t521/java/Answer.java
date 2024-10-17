package org.real.temp;

import java.util.*;
import java.util.regex.*;

public class Answer {

    /**
     * Counts the occurrences of specified words in the given text.
     *
     * This function filters the words from the text based on the provided list,
     * counts their occurrences, and returns a map with the words in the
     * order they were provided.
     *
     * @param text The input text from which to count words.
     * @param filterWords A list of words to filter and count.
     * @return A map with the count of each filter word in the text,
     *         maintaining the order from filterWords.
     */
    public static Map<String, Integer> wordFilterCounter(String text, List<String> filterWords) {
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

    public static void main(String[] args) {
        String text = "This is a sample text. It contains some words like 'sample', 'text', and 'words'.";
        List<String> filterWords = Arrays.asList("sample", "text", "words");

        Map<String, Integer> result = wordFilterCounter(text, filterWords);
        System.out.println(result);
    }
}