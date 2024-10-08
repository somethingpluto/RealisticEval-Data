package org.real.temp;

import java.util.Arrays;

public class Answer {
    /**
     * Calculates the rotation matrix required to rotate from vector "from" to vector "to".
     * The method uses the Rodrigues' rotation formula for this purpose.
     *
     * @param from the starting vector, must be a non-zero vector.
     * @param to the target vector, must be a non-zero vector.
     * @return a 3x3 rotation matrix that when multiplied by "from" aligns it with "to".
     */
    public static double[][] calculateRotationMatrix(double[] from, double[] to) {
        if (from.length != 3 || to.length != 3) {
            throw new IllegalArgumentException("Both vectors must be three-dimensional.");
        }

        // Normalize vectors to ensure calculations for unit vectors
        double[] u = normalizeVector(from);
        double[] v = normalizeVector(to);

        // Cross product u x v
        double[] axis = crossProduct(u, v);

        // Dot product u . v
        double angle = Math.acos(dotProduct(u, v));

        // Using Rodrigues' rotation formula
        double[][] identityMatrix = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        double[][] kMatrix = new double[][]{
            {0, -axis[2], axis[1]},
            {axis[2], 0, -axis[0]},
            {-axis[1], axis[0], 0}
        };
        double[][] kMatrixSquared = matrixMultiply(kMatrix, kMatrix);

        double cosTheta = Math.cos(angle);
        double sinTheta = Math.sin(angle);

        return addMatrices(addMatrices(identityMatrix, scalarMultiply(kMatrix, sinTheta)),
                           scalarMultiply(kMatrixSquared, 1 - cosTheta));
    }

    private static double[] crossProduct(double[] a, double[] b) {
        return new double[]{
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        };
    }

    private static double dotProduct(double[] a, double[] b) {
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    }

    private static double[][] addMatrices(double[][] a, double[][] b) {
        double[][] result = new double[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                result[i][j] = a[i][j] + b[i][j];
            }
        }
        return result;
    }

    private static double[][] scalarMultiply(double[][] matrix, double scalar) {
        double[][] result = new double[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                result[i][j] = matrix[i][j] * scalar;
            }
        }
        return result;
    }

    private static double[] normalizeVector(double[] vector) {
        double length = Math.sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]);
        return new double[]{vector[0] / length, vector[1] / length, vector[2] / length};
    }

    private static double[][] matrixMultiply(double[][] a, double[][] b) {
        double[][] result = new double[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        double[] from = {1, 0, 0};
        double[] to = {0, 1, 0};
        double[][] rotationMatrix = calculateRotationMatrix(from, to);
        System.out.println("Rotation Matrix:");
        for (double[] row : rotationMatrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
