package org.real.temp;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import org.apache.commons.lang3.tuple.Pair;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.math3.util.Pair;

public class Answer {

    /**
     * Fills missing values in the specified column of the DataFrame with the first valid value in that column.
     *
     * @param dataFrame The DataFrame represented as a List of Pairs.
     * @param columnName The name of the column to fill missing values.
     * @return The DataFrame with missing values filled.
     */
    public static List<Pair<String, String>> fillMissingWithFirstValid(List<Pair<String, String>> dataFrame, String columnName) {
        if (dataFrame == null || dataFrame.isEmpty()) {
            throw new IllegalArgumentException("DataFrame cannot be null or empty.");
        }

        boolean columnExists = false;
        String firstValidValue = null;

        // Check if the column exists and find the first valid value
        for (Pair<String, String> row : dataFrame) {
            if (row.getValue() != null && row.getValue().equals(columnName)) {
                columnExists = true;
                if (firstValidValue == null && row.getKey() != null) {
                    firstValidValue = row.getKey();
                }
            }
        }

        if (!columnExists) {
            throw new IllegalArgumentException("Column '" + columnName + "' does not exist in the DataFrame.");
        }

        // Fill missing values in the specified column with the first valid value
        for (Pair<String, String> row : dataFrame) {
            if (row.getValue().equals(columnName) && row.getKey() == null) {
                row = Pair.of(firstValidValue, row.getValue());
            }
        }

        return dataFrame;
    }

    public static void main(String[] args) {
        // Example usage
        List<Pair<String, String>> dataFrame = Arrays.asList(
            Pair.of(null, "A"),
            Pair.of("B1", "B"),
            Pair.of(null, "A"),
            Pair.of("C1", "C")
        );

        String columnName = "A";
        List<Pair<String, String>> updatedDataFrame = fillMissingWithFirstValid(dataFrame, columnName);

        // Print the updated DataFrame
        for (Pair<String, String> row : updatedDataFrame) {
            System.out.println(row);
        }
    }
}