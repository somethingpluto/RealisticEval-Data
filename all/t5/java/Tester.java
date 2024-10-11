package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testMatrixMultiply() {
        // Test data
        int[][] matrixA = {
            {1, 2},
            {3, 4}
        };
        int[][] matrixB = {
            {5, 6},
            {7, 8}
        };
        int[][] expectedOutput = {
            {19, 22},
            {43, 50}
        };

        // Call the method under test
        int[][] result = matrixMultiply(matrixA, matrixB);

        // Verify the result
        assertEquals(expectedOutput.length, result.length);
        for (int i = 0; i < expectedOutput.length; i++) {
            assertEquals(expectedOutput[i].length, result[i].length);
            for (int j = 0; j < expectedOutput[i].length; j++) {
                assertEquals(expectedOutput[i][j], result[i][j]);
            }
        }
    }

    // Method under test
    public int[][] matrixMultiply(int[][] matrixA, int[][] matrixB) {
        int rowsA = matrixA.length;
        int colsA = matrixA[0].length;
        int rowsB = matrixB.length;
        int colsB = matrixB[0].length;

        if (colsA != rowsB) {
            throw new IllegalArgumentException("Number of columns in matrixA must be equal to number of rows in matrixB");
        }

        int[][] result = new int[rowsA][colsB];

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        return result;
    }
}