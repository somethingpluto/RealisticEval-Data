package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class Tester {

    @Test
    public void testGetRotation() {
        // Assuming we have a way to create a rotation matrix and expected result
        double[][] matrix = { {Math.cos(Math.PI / 4), -Math.sin(Math.PI / 4), 0},
                              {Math.sin(Math.PI / 4), Math.cos(Math.PI / 4), 0},
                              {0, 0, 1} };
        double expectedResult = Math.PI / 4;

        double actualResult = getRotation(np.array(matrix));

        assertEquals(expectedResult, actualResult, 0.0001);
    }

    private double getRotation(double[][] matrix) {
        /*
         * Implement the logic to extract the rotation angle from the given matrix.
         * This is just a placeholder implementation.
         */
        double cosTheta = matrix[0][0];
        double sinTheta = matrix[1][0];
        return Math.atan2(sinTheta, cosTheta);
    }
}
