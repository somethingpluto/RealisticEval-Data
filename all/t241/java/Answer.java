package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Answer {

    public static Tuple getMinSeqNumAndDistance(String filePath, String word1, String word2) {
        int minDistance = Integer.MAX_VALUE;
        Integer minSeqNum = null;
        int currentLineNumber = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] words = line.trim().split("\\s+");
                int[] word1Indices = findIndices(words, word1);
                int[] word2Indices = findIndices(words, word2);

                for (int index1 : word1Indices) {
                    for (int index2 : word2Indices) {
                        int distance = Math.abs(index1 - index2);
                        if (distance < minDistance) {
                            minDistance = distance;
                            minSeqNum = currentLineNumber;
                        }
                    }
                }

                currentLineNumber++;
            }
        } catch (IOException e) {
            System.out.println("Error: The file " + filePath + " does not exist.");
            return new Tuple(null, Integer.MAX_VALUE);
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            return new Tuple(null, Integer.MAX_VALUE);
        }

        return new Tuple(minSeqNum, minDistance);
    }

    private static int[] findIndices(String[] words, String targetWord) {
        int[] indices = new int[words.length];
        int count = 0;

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(targetWord)) {
                indices[count++] = i;
            }
        }

        return java.util.Arrays.copyOf(indices, count);
    }

    public static class Tuple {
        private final Integer lineNumber;
        private final int distance;

        public Tuple(Integer lineNumber, int distance) {
            this.lineNumber = lineNumber;
            this.distance = distance;
        }

        public Integer getLineNumber() {
            return lineNumber;
        }

        public int getDistance() {
            return distance;
        }

        @Override
        public String toString() {
            return "(" + lineNumber + ", " + distance + ")";
        }
    }

    public static void main(String[] args) {
        // Example usage
        Tuple result = getMinSeqNumAndDistance("path/to/your/file.txt", "word1", "word2");
        System.out.println(result);
    }
}