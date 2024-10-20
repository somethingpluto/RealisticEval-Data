import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;

package org.real.temp;

public class Answer {
    
    /**
     * Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
     *
     * @param filePath Path to the CSV file opened in read-plus mode.
     * @param rowCandidate List containing the new row to be appended.
     */
    public static void appendOrSkipRow(String filePath, List<String> rowCandidate) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath));
             PrintWriter writer = new PrintWriter(new FileWriter(filePath, true))) {
            
            // Read existing rows into a list
            List<List<String>> existingRows = new ArrayList<>();
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                existingRows.add(new ArrayList<>(List.of(parts)));
            }

            // Check if a matching row exists in the first three columns
            for (List<String> row : existingRows) {
                if (row.size() >= 3 && row.subList(0, 3).equals(rowCandidate.subList(0, 3))) {
                    System.out.println("Row already exists. Skipping append.");
                    return;  // Skip appending if a match is found
                }
            }

            // Append the new row if no matching row is found
            writer.println();  // Ensure there's a newline before appending
            writer.println(String.join(",", rowCandidate));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Example usage
        List<String> rowCandidate = List.of("value1", "value2", "value3");
        String filePath = "path/to/your/file.csv";
        appendOrSkipRow(filePath, rowCandidate);
    }
}