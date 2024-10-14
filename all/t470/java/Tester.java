package org.real.temp;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testApplyShearX() {
        // Define the input matrix and expected output matrix
        double[][] inputMatrix = {{1, 2}, {3, 4}};
        double shearFactor = 0.5; // Example shear factor
        double[][] expectedOutputMatrix = {{1 + 0.5 * 2, 2}, {3 + 0.5 * 4, 4}};

        // Call the method under test
        double[][] resultMatrix = applyShearX(inputMatrix, shearFactor);

        // Assert that the result matches the expected output
        assertArrayEquals(expectedOutputMatrix, resultMatrix);
    }

    // Dummy implementation of applyShearX for demonstration purposes
    private double[][] applyShearX(double[][] matrix, double shearFactor) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] result = new double[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix[i][j] + shearFactor * matrix[i][j];
            }
        }

        return result;
    }
}
