package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static void main(String[] args) {
        String csvFilePath = "path/to/your/csvfile.csv";
        System.out.println(csvToSqlInsert(csvFilePath));
    }

    public static String csvToSqlInsert(String csvFilePath) {
        // Extract the table name from the CSV file name, removing the suffix
        Path path = Paths.get(csvFilePath);
        String tableName = Files.getFileStore(path).name().replaceFirst("[.][^.]+$", "");

        // Open the CSV file and read its contents
        List<String> insertStatements = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(csvFilePath))) {
            String line = reader.readLine(); // Skip the first line (header)
            if (line != null) {
                String[] headers = line.split(",");
                
                String currentLine;
                while ((currentLine = reader.readLine()) != null) {
                    String[] row = currentLine.split(",");
                    List<String> values = new ArrayList<>();
                    
                    for (String value : row) {
                        // Handle different types of values (e.g., strings, numbers)
                        if (value.matches("\\d+")) {  // If value is a digit, no quotes needed
                            values.add(value);
                        } else {  // Assume it's a string otherwise
                            String escapedValue = value.replace("'", "''");  // Escape single quotes
                            values.add("'" + escapedValue + "'");  // Use double quotes outside
                        }
                    }

                    // Join column names and values to form an INSERT statement
                    String insertStatement = String.format("INSERT INTO %s (%s) VALUES (%s);",
                            tableName,
                            String.join(", ", headers),
                            String.join(", ", values));
                    insertStatements.add(insertStatement);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Combine all insert statements into a single output
        return String.join("\n", insertStatements);
    }
}