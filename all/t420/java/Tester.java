package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.stubbing.Answer;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

public class Tester {

    @Mock
    private BufferedReader mockReader;

    private List<List<String>> sequences;

    @Before
    public void setUp() throws IOException {
        MockitoAnnotations.initMocks(this);
        sequences = new ArrayList<>();
    }

    @Test
    public void testSimpleCase() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello world", "hello hello world", "world hello", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 1), result);
    }

    @Test
    public void testMultipleLines() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello planet", "world hello planet", "hello world planet", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(1, 1), result);
    }

    @Test
    public void testLargeDistance() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn(
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world", null
        );

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 27), result);
    }

    @Test
    public void testAdjacentWords() throws IOException {
        // Mock the file read operation
        when(mockReader.readLine()).thenReturn("hello world", "hello hello world world", "world hello", null);

        List<List<String>> sequences = readFileAsSequences(mockReader);
        Pair<Integer, Integer> result = getMinDistance(sequences, "hello", "world");

        assertEquals(new Pair<>(0, 1), result);
    }

    // Utility class to represent a pair of values
    public static class Pair<T1, T2> {
        private T1 first;
        private T2 second;

        public Pair(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }

        @Override
        public String toString() {
            return "(" + first + ", " + second + ")";
        }
    }

    // Method to read the file and convert each line into a list of words
    private List<List<String>> readFileAsSequences(BufferedReader reader) throws IOException {
        List<List<String>> sequences = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            String[] words = line.trim().split("\\s+");
            List<String> wordList = new ArrayList<>();
            for (String word : words) {
                wordList.add(word);
            }
            sequences.add(wordList);
        }
        return sequences;
    }

    // Method to find the minimum distance between two words in a list of sequences
    private Pair<Integer, Integer> getMinDistance(List<List<String>> sequences, String word1, String word2) {
        int minDistance = Integer.MAX_VALUE;
        Integer minSeqNum = null;

        for (int i = 0; i < sequences.size(); i++) {
            List<String> seq = sequences.get(i);
            int distance = findClosestWordIndices(seq, word1, word2);
            if (distance < minDistance) {
                minDistance = distance;
                minSeqNum = i;
            }
        }

        if (minDistance == Integer.MAX_VALUE) {
            return new Pair<>(null, null);
        } else {
            return new Pair<>(minSeqNum, minDistance);
        }
    }

    // Method to find the closest word indices in a sequence
    private int findClosestWordIndices(List<String> sequence, String word1, String word2) {
        List<Integer> word1Indices = new ArrayList<>();
        List<Integer> word2Indices = new ArrayList<>();
        int minDistance = Integer.MAX_VALUE;

        for (int index = 0; index < sequence.size(); index++) {
            String word = sequence.get(index);
            if (word.equals(word1)) {
                word1Indices.add(index);
            } else if (word.equals(word2)) {
                word2Indices.add(index);
            }
        }

        for (int index1 : word1Indices) {
            for (int index2 : word2Indices) {
                int distance = Math.abs(index1 - index2);
                if (distance < minDistance) {
                    minDistance = distance;
                }
            }
        }

        return minDistance;
    }
}
