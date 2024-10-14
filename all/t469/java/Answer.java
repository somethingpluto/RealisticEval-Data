package org.real.temp;

public class Answer {

    public static double[] getScale(double[][] matrix) {
        if (matrix.length != 3 || matrix[0].length != 3 || matrix[1].length != 3 || matrix[2].length != 3) {
            throw new IllegalArgumentException("Input must be a 3x3 matrix");
        }

        double scaleX = Math.sqrt(Math.pow(matrix[0][0], 2) + Math.pow(matrix[0][1], 2));
        double scaleY = Math.sqrt(Math.pow(matrix[1][0], 2) + Math.pow(matrix[1][1], 2));

        return new double[]{scaleX, scaleY};
    }
}
