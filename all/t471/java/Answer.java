package org.real.temp;

import java.lang.Math;

/**
 * This class provides a method to calculate the rotation angle in radians from a 3x3 affine transformation matrix.
 */
public class Answer {

    /**
     * Calculates the rotation angle in radians from a given 3x3 affine transformation matrix.
     * 
     * @param matrix A 2D affine transformation matrix represented as a 2D double array.
     * @return The rotation angle in radians.
     * @throws IllegalArgumentException If the input matrix is not a 3x3 matrix.
     */
    public static double getRotation(double[][] matrix) {
        // Ensure the matrix is a 3x3 array
        if (matrix == null || matrix.length != 3 || matrix[0].length != 3 || matrix[1].length != 3 || matrix[2].length != 3) {
            throw new IllegalArgumentException("Input must be a 3x3 affine transformation matrix.");
        }

        // Calculate the rotation angle using atan2
        double rotationAngle = Math.atan2(matrix[1][0], matrix[0][0]);

        return rotationAngle;
    }

    // Example usage
    public static void main(String[] args) {
        double[][] matrix = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {0.0, 0.0, 1.0}
        };

        double angle = getRotation(matrix);
        System.out.println("Rotation Angle: " + angle);
    }
}