package org.real.temp;

public class Answer {

    /**
     * Calculates the maximum width for each column in a given 2D array of strings.
     * 
     * @param data A 2D array of strings representing the table data.
     * @return An array of integers representing the maximum width for each column.
     */
    public static int[] calculateColumnWidths(String[][] data) {
        // Initialize an array to hold the maximum widths for each column.
        // Assumes all rows in data have the same number of columns.
        int[] widths = new int[data[0].length];

        // Iterate over each row in the data.
        for (String[] row : data) {
            // Iterate over each column in the row.
            for (int idx = 0; idx < row.length; idx++) {
                // Update the width at index `idx` with the maximum of the current width
                // and the length of the string in the current column.
                widths[idx] = Math.max(widths[idx], row[idx].length());
            }
        }

        // Return the array of maximum widths for each column.
        return widths;
    }

    // Example usage
    public static void main(String[] args) {
        String[][] data = {
            {"apple", "banana", "cherry"},
            {"orange", "grape", "mango"},
            {"kiwi", "pineapple", "strawberry"}
        };

        int[] widths = calculateColumnWidths(data);
        for (int width : widths) {
            System.out.println(width);
        }
    }
}