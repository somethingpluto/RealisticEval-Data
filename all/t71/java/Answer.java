package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Reads numerical columns from a file starting from the line after the last line containing '/'.
     *
     * @param fileName The name of the file to read.
     * @return A 2D array containing the numerical question.
     * @throws IllegalArgumentException If the file does not contain any '/' character.
     */
    public static double[][] readColumns(String fileName) throws IOException {
        // Initialize a variable to track the last slash line index
        Integer lastSlashIndex = null;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            List<String> lines = new ArrayList<>();

            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }

            // Find the index of the last line that contains the "/" character
            for (int i = 0; i < lines.size(); i++) {
                if (lines.get(i).contains("/")) {
                    lastSlashIndex = i;
                }
            }

            // If no "/" character was found, throw an error
            if (lastSlashIndex == null) {
                throw new IllegalArgumentException("File does not contain '/' character");
            }

            // Read the remaining lines in the file, starting from the line after the last "/"
            List<String> dataLines = new ArrayList<>();
            for (int i = lastSlashIndex + 1; i < lines.size(); i++) {
                String currentLine = lines.get(i).trim();
                if (!currentLine.isEmpty() && !currentLine.startsWith("!")) {
                    dataLines.add(currentLine);
                }
            }

            // If no valid lines remain, return an empty array
            if (dataLines.isEmpty()) {
                return new double[0][0];
            }

            // Get the row and column count by counting the number of columns in the first line
            int colCount = dataLines.get(0).split(" ").length;

            // Create an empty 2D array of the required size
            double[][] arr = new double[dataLines.size()][colCount];

            // Loop through the lines in the file
            for (int i = 0; i < dataLines.size(); i++) {
                // Split the line into numbers and convert them to floats
                String[] nums = dataLines.get(i).split(" ");
                for (int j = 0; j < nums.length; j++) {
                    arr[i][j] = Double.parseDouble(nums[j]);
                }
            }

            // Return the array
            return arr;
        }
    }

    public static void main(String[] args) {
        try {
            double[][] result = readColumns("example.txt");
            // Print the result or perform further operations
            for (double[] row : result) {
                for (double num : row) {
                    System.out.print(num + " ");
                }
                System.out.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}