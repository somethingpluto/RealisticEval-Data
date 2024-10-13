package org.real.temp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Answer {

    /**
     * Parses a Markdown formatted table into a list of arrays, each array representing a row.
     *
     * @param mdTable A string representing a Markdown table.
     * @return A list where each array represents a row in the table.
     */
    public static List<String[]> parseMarkdownTable(String mdTable) {
        // Split the input string into lines and strip whitespace
        String[] lines = mdTable.trim().split("\n");

        // Filter out the separator line for the header (which usually contains "---")
        List<String> filteredLines = new ArrayList<>();
        for (String line : lines) {
            if (!line.trim().contains("---")) {
                filteredLines.add(line);
            }
        }

        // Initialize the list to store each row as an array
        List<String[]> tableData = new ArrayList<>();

        // Process each line
        for (String line : filteredLines) {
            // Strip leading and trailing spaces and pipes, then split by "|"
            String[] row = line.trim().replaceAll("^\\|+|\\|+$", "").split("\\|");
            
            // Process each cell, strip spaces, handle empty cells, and add to the list
            String[] tupleRow = Arrays.stream(row)
                                      .map(cell -> cell.trim().isEmpty() ? "" : cell.trim())
                                      .toArray(String[]::new);
            
            // Add the array to the list
            tableData.add(tupleRow);
        }

        return tableData;
    }

    public static void main(String[] args) {
        String markdownTable = "| Header1 | Header2 |\n" +
                               "| --- | --- |\n" +
                               "| Row1 Cell1 | Row1 Cell2 |\n" +
                               "| Row2 Cell1 | Row2 Cell2 |";

        List<String[]> result = parseMarkdownTable(markdownTable);
        for (String[] row : result) {
            System.out.println(Arrays.toString(row));
        }
    }
}