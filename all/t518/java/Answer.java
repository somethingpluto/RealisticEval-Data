package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Convert numeric values in a CSV row from string format to a standardized format.
     *
     * @param row A map representing a row of CSV data where keys are column names and values are strings.
     * @return A new map with values converted:
     *         - Numeric strings have commas replaced with dots.
     *         - Non-numeric strings are set to null.
     */
    public static Map<String, String> convertCsvValues(Map<String, String> row) {
        Map<String, String> convertedRow = new HashMap<>();

        for (Map.Entry<String, String> entry : row.entrySet()) {
            String key = entry.getKey();
            String value = entry.getValue();

            // Check if the value is numeric with possible comma and negative sign
            boolean isNumeric = value.replace(",", "").replace("-", "").matches("[0-9]+");

            if (isNumeric) {
                // Replace comma with dot for numeric conversion
                convertedRow.put(key, value.replace(',', '.'));
            } else {
                // Set to null if not a valid number
                convertedRow.put(key, null);
            }
        }

        return convertedRow;
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, String> row = new HashMap<>();
        row.put("id", "123");
        row.put("name", "John Doe");
        row.put("amount", "1,234.56");
        row.put("status", "active");

        Map<String, String> convertedRow = convertCsvValues(row);
        System.out.println(convertedRow);
    }
}