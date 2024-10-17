package org.real.temp;

import java.util.Arrays;

public class Answer {

    /**
     * Scale the point cloud by a given factor.
     *
     * @param pointCloud A 2D array representing the 3D point cloud with shape (N, 3).
     * @param scaleFactor A double representing the scaling factor.
     * @return A 2D array of the scaled point cloud with shape (N, 3).
     * @throws IllegalArgumentException If the point cloud is not a 2D array with shape (N, 3).
     */
    public static double[][] scalePointCloud(double[][] pointCloud, double scaleFactor) {
        // Ensure pointCloud is a 2D array
        if (pointCloud == null || pointCloud.length == 0 || pointCloud[0].length != 3) {
            throw new IllegalArgumentException("pointCloud must be a 2D array with shape (N, 3)");
        }

        // Scale the point cloud by the given factor
        double[][] scaledPointCloud = new double[pointCloud.length][3];
        for (int i = 0; i < pointCloud.length; i++) {
            scaledPointCloud[i] = Arrays.stream(pointCloud[i])
                                        .map(x -> x * scaleFactor)
                                        .toArray();
        }

        return scaledPointCloud;
    }

    public static void main(String[] args) {
        // Example usage
        double[][] pointCloud = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0}
        };
        double scaleFactor = 2.0;

        double[][] scaledPointCloud = scalePointCloud(pointCloud, scaleFactor);
        for (double[] row : scaledPointCloud) {
            System.out.println(Arrays.toString(row));
        }
    }
}