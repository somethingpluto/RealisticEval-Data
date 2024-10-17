package org.real.temp;

public class Answer {

    /**
     * Flip the point cloud across a specified axis.
     *
     * @param pointCloud A N x 3 array representing the 3D point cloud.
     * @param axis       An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).
     * @return A N x 3 array of the flipped point cloud.
     */
    public static double[][] flipPointCloud(double[][] pointCloud, int axis) {
        // Validate the axis input
        if (axis < 0 || axis > 2) {
            throw new IllegalArgumentException("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).");
        }

        // Create a scaling factor array with -1 for the specified axis and 1 for others
        double[] flipFactors = new double[pointCloud[0].length];
        for (int i = 0; i < pointCloud[0].length; i++) {
            flipFactors[i] = (i == axis) ? -1 : 1;
        }

        // Flip the point cloud by multiplying with the scaling factor array
        double[][] flippedPointCloud = new double[pointCloud.length][pointCloud[0].length];
        for (int i = 0; i < pointCloud.length; i++) {
            for (int j = 0; j < pointCloud[0].length; j++) {
                flippedPointCloud[i][j] = pointCloud[i][j] * flipFactors[j];
            }
        }

        return flippedPointCloud;
    }

    public static void main(String[] args) {
        // Example usage
        double[][] pointCloud = {
            {1, 2, 3},
            {4, 5, 6}
        };

        int axis = 1; // Flip along the y-axis

        double[][] flippedPointCloud = flipPointCloud(pointCloud, axis);

        // Print the flipped point cloud
        for (double[] row : flippedPointCloud) {
            for (double value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}