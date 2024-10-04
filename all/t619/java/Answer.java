package org.real.temp;

public class Answer {

    /**
     * Multiplies two matrices.
     *
     * @param matrixA the first matrix
     * @param matrixB the second matrix
     * @return the resulting matrix after multiplication
     * @throws IllegalArgumentException if the matrices are incompatible for multiplication
     */
    public static double[][] multiplyMatrix(double[][] matrixA, double[][] matrixB) {
        // Get dimensions of the input matrices
        int rowsA = matrixA.length;         // Number of rows in matrixA
        int colsA = matrixA[0].length;      // Number of columns in matrixA
        int rowsB = matrixB.length;         // Number of rows in matrixB
        int colsB = matrixB[0].length;      // Number of columns in matrixB

        // Validate matrix dimensions for multiplication
        if (rowsB != colsA) {
            throw new IllegalArgumentException("Incompatible matrix dimensions for multiplication");
        }

        // Initialize the result matrix
        double[][] result = new double[rowsA][colsB];

        // Perform matrix multiplication
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        return result;  // Return the resulting matrix
    }
}
