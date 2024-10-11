package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Parses a Markdown formatted table into a list of string arrays,
     * each array representing a row.
     *
     * @param mdTable A string representing a Markdown table.
     * @return A list of string arrays where each array represents a row in the table.
     */
    public static List<String[]> parseMarkdownTable(String mdTable) {
        // Split the input string into lines and trim whitespace
        String[] lines = mdTable.trim().split("\n");

        // Initialize the list to store each row as an array
        List<String[]> tableData = new ArrayList<>();

        // Process each line
        for (String line : lines) {
            // Trim leading and trailing spaces and pipes, then split by "|"
            String trimmedLine = line.trim().replaceAll("^\\||\\|$", ""); // Remove leading/trailing pipes
            String[] row = trimmedLine.split("\\|");

            // Process each cell, strip spaces, handle empty cells
            for (int i = 0; i < row.length; i++) {
                row[i] = row[i].trim(); // Strip leading and trailing spaces from each cell
            }

            // Filter out the separator line (which usually contains "---")
            if (!trimmedLine.contains("---")) {
                tableData.add(row);
            }
        }

        return tableData;
    }

    // Method to print the parsed table for verification
    public static void printTable(List<String[]> table) {
        for (String[] row : table) {
            System.out.print("| ");
            for (String cell : row) {
                System.out.print(cell + " | ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        String mdTable = "| Name     | Age | Occupation   |\n" +
                         "|----------|-----|--------------|\n" +
                         "| Alice    | 30  | Engineer     |\n" +
                         "| Bob      | 25  | Designer     |\n" +
                         "| Charlie  | 35  | Manager      |\n" +
                         "|          |     |              |";

        List<String[]> parsedTable = parseMarkdownTable(mdTable);
        printTable(parsedTable);
    }
}
