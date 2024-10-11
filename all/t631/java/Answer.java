package org.real.temp;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Answer {

    /**
     * Formats a list of strings into a single-line CSV string and writes it to a specified file.
     *
     * @param strings List of strings to be formatted into CSV.
     * @param filePath The file path where the CSV string should be written.
     */
    public void writeCsvToFile(List<String> strings, String filePath) {
        // Join the list of strings into a single line CSV formatted string
        String csvString = String.join(",", strings);

        // Write the CSV string to the specified file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(csvString);
            System.out.println("CSV written to file: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example usage
        Answer answer = new Answer();
        List<String> data = List.of("Apple", "Banana", "Cherry", "Date");
        String filePath = "output.csv"; // Specify your desired file path here
        answer.writeCsvToFile(data, filePath);
    }
}