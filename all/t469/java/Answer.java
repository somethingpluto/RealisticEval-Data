package org.real.temp;

import java.util.Arrays;

public class Answer {

    /**
     * Given a 3x3 affine transformation matrix, return the corresponding scaling factors
     * along the x and y axes.
     *
     * @param matrix A 3x3 affine transformation matrix represented as a flat array.
     * @return An array containing the scale factors (scale_x, scale_y).
     * @throws IllegalArgumentException If the input is not a 3x3 matrix.
     */
    public static double[] getScale(double[] matrix) {
        // Ensure the matrix is a 3x3 array
        if (matrix == null || matrix.length != 9) {
            throw new IllegalArgumentException("Input must be a 3x3 affine transformation matrix.");
        }

        // Extract the relevant sub-matrices for calculating scale factors
        double[] subMatrixX = Arrays.copyOfRange(matrix, 0, 2);
        double[] subMatrixY = Arrays.copyOfRange(matrix, 3, 5);

        // Calculate the scale factors using the norm of the columns
        double scaleX = calculateNorm(subMatrixX);
        double scaleY = calculateNorm(subMatrixY);

        return new double[]{scaleX, scaleY};
    }

    /**
     * Helper method to calculate the Euclidean norm of a vector.
     *
     * @param vector The vector for which to calculate the norm.
     * @return The Euclidean norm of the vector.
     */
    private static double calculateNorm(double[] vector) {
        double sumOfSquares = 0.0;
        for (double value : vector) {
            sumOfSquares += value * value;
        }
        return Math.sqrt(sumOfSquares);
    }

    // Example usage
    public static void main(String[] args) {
        double[] matrix = {1, 0, 0, 0, 1, 0, 0, 0, 1};
        double[] scales = getScale(matrix);
        System.out.println("Scale X: " + scales[0]);
        System.out.println("Scale Y: " + scales[1]);
    }
}