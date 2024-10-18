package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<List<String>> readFileAsSequences(String filePath) {
        List<List<String>> sequences = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] words = line.trim().split("\\s+");
                List<String> wordList = new ArrayList<>();
                for (String word : words) {
                    wordList.add(word);
                }
                sequences.add(wordList);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sequences;
    }

    public static int findClosestWordIndices(List<String> sequence, String word1, String word2) {
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

    public static Pair<Integer, Integer> getMinDistance(String filePath, String word1, String word2) {
        List<List<String>> sequences = readFileAsSequences(filePath);
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

}