package org.real.temp;

import java.util.List;
import java.util.ArrayList;

public class Answer {
    /**
     * Transpose a given matrix (2D array).
     *
     * @param matrix The input 2D array to be transposed.
     * @return The transposed 2D array.
     */
    public static List<List<Integer>> transposeMatrix(List<List<Integer>> matrix) {
        // Check if the matrix is empty
        if (matrix == null || matrix.isEmpty() || matrix.get(0).isEmpty()) {
            return new ArrayList<>();
        }

        int numRows = matrix.size();
        int numCols = matrix.get(0).size();

        // Initialize the transposed matrix with the correct dimensions
        List<List<Integer>> transposed = new ArrayList<>();
        for (int col = 0; col < numCols; col++) {
            List<Integer> newRow = new ArrayList<>(numRows);
            for (int row = 0; row < numRows; row++) {
                newRow.add(0);
            }
            transposed.add(newRow);
        }

        // Populate the transposed matrix
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                transposed.get(j).set(i, matrix.get(i).get(j));
            }
        }

        return transposed;
    }

    public static void main(String[] args) {
        // Example usage
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(List.of(1, 2, 3));
        matrix.add(List.of(4, 5, 6));
        matrix.add(List.of(7, 8, 9));

        List<List<Integer>> transposedMatrix = transposeMatrix(matrix);
        System.out.println(transposedMatrix);
    }
}