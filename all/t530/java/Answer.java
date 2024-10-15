package org.real.temp;

import java.util.Arrays;

public class Answer {
    public static int[][] createMatrix(int rows, int columns, int initialValue) {
        // Initialize the matrix
        int[][] matrix = new int[rows][columns];

        // Loop through each row
        for (int i = 0; i < rows; i++) {
            // Loop through each column and fill the row with the initial value
            Arrays.fill(matrix[i], initialValue);
        }

        return matrix;
    }

    public static void main(String[] args) {
        int rows = 3;
        int columns = 4;
        int initialValue = 0;

        int[][] matrix = createMatrix(rows, columns, initialValue);

        // Print the matrix
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}