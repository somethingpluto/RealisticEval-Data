package org.real.temp;

import java.util.Arrays;

public class Answer {

    /**
     * Given a 3x3 matrix, return the corresponding translation vector.
     *
     * @param matrix A 3x3 affine transformation matrix.
     * @return A 2-element array containing the translation components (translation_x, translation_y).
     */
    public static double[] getTranslation(double[][] matrix) {
        if (matrix == null || matrix.length != 3 || matrix[0].length != 3 || matrix[1].length != 3 || matrix[2].length != 3) {
            throw new IllegalArgumentException("Input must be a 3x3 matrix.");
        }

        // Extract the translation components from the last row of the matrix
        double translationX = matrix[2][0];
        double translationY = matrix[2][1];

        return new double[]{translationX, translationY};
    }

    public static void main(String[] args) {
        double[][] matrix = {
            {1, 0, 5},
            {0, 1, 10},
            {0, 0, 1}
        };

        double[] translation = getTranslation(matrix);
        System.out.println(Arrays.toString(translation)); // Output should be [5.0, 10.0]
    }
}