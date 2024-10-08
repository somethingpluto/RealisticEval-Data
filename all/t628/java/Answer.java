package org.real.temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;

public class Answer {

    /**
     * Modifies a specific line in the given file.
     *
     * @param filePath the path of the file to be modified
     * @param lineNumber the line number to be modified (1-based index)
     * @param newValue the new value to update the line with
     * @throws IOException if an I/O error occurs
     */
    public void modifyLineInFile(String filePath, int lineNumber, String newValue) throws IOException {
        // Read the current lines of the file
        List<String> lines = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        }

        // Check if the line number is valid
        if (lineNumber < 1 || lineNumber > lines.size()) {
            throw new IllegalArgumentException("Invalid line number: " + lineNumber);
        }

        // Update the specific line with the new value
        lines.set(lineNumber - 1, newValue);

        // Write the updated lines back to the file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        Answer answer = new Answer();
        String filePath = "example.txt"; // Specify your file path
        int lineNumber = 2; // Specify which line to modify
        String newValue = "This is the new content for line 2."; // New content

        try {
            answer.modifyLineInFile(filePath, lineNumber, newValue);
            System.out.println("Line modified successfully.");
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}