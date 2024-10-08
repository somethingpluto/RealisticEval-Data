package org.real.temp;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Reads a CSV file and parses each line into a list of strings.
     *
     * @param filePath The path to the CSV file.
     * @return A list of string arrays, where each array represents a line from the CSV.
     * @throws IOException If there is an error reading the file.
     */
    public List<List<String>> readCsv(String filePath) throws IOException {
        List<List<String>> csvData = new ArrayList<>();

        // Read all lines from the specified CSV file
        List<String> lines = Files.readAllLines(Paths.get(filePath));

        // Parse each line into a list of strings
        for (String line : lines) {
            // Split the line by commas and store it in a List
            List<String> parsedLine = List.of(line.split(","));
            csvData.add(parsedLine);
        }

        return csvData;
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        String pathToCsv = "path/to/your/file.csv"; // Change to your CSV file path

        try {
            List<List<String>> result = answer.readCsv(pathToCsv);
            // Print the result for demonstration
            for (List<String> row : result) {
                System.out.println(row);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}