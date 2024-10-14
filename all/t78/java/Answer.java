package org.real.temp;

public class Answer {

    /**
     * Convert Euler angles (roll, pitch, yaw) to a rotation matrix.
     *
     * @param roll  Rotation around the x-axis in degrees.
     * @param pitch Rotation around the y-axis in degrees.
     * @param yaw   Rotation around the z-axis in degrees.
     * @return A 3x3 rotation matrix.
     */
    public static double[][] eulerToRotationMatrix(double roll, double pitch, double yaw) {
        // Convert degrees to radians
        roll = Math.toRadians(roll);
        pitch = Math.toRadians(pitch);
        yaw = Math.toRadians(yaw);

        // Rotation matrix around x-axis (roll)
        double[][] Rx = {
            {1, 0, 0},
            {0, Math.cos(roll), -Math.sin(roll)},
            {0, Math.sin(roll), Math.cos(roll)}
        };

        // Rotation matrix around y-axis (pitch)
        double[][] Ry = {
            {Math.cos(pitch), 0, Math.sin(pitch)},
            {0, 1, 0},
            {-Math.sin(pitch), 0, Math.cos(pitch)}
        };

        // Rotation matrix around z-axis (yaw)
        double[][] Rz = {
            {Math.cos(yaw), -Math.sin(yaw), 0},
            {Math.sin(yaw), Math.cos(yaw), 0},
            {0, 0, 1}
        };

        // Combined rotation matrix, R = Rz * Ry * Rx
        double[][] R = multiplyMatrices(multiplyMatrices(Rz, Ry), Rx);

        return R;
    }

    /**
     * Multiplies two matrices.
     *
     * @param a First matrix.
     * @param b Second matrix.
     * @return The result of multiplying the two matrices.
     */
    private static double[][] multiplyMatrices(double[][] a, double[][] b) {
        int rowsA = a.length;
        int colsA = a[0].length;
        int rowsB = b.length;
        int colsB = b[0].length;

        if (colsA != rowsB) {
            throw new IllegalArgumentException("The number of columns in the first matrix must equal the number of rows in the second matrix.");
        }

        double[][] result = new double[rowsA][colsB];

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        return result;
    }
}