package org.real.temp;

import org.apache.commons.math3.linear.*;

public class Answer {

    public static double[][] transformPointCloudToReferenceFrame(double[][] pointCloud, double[][] refFramePoints) {
        // Unpack the three points defining the new reference frame
        double[] A = refFramePoints[0];
        double[] B = refFramePoints[1];
        double[] C = refFramePoints[2];

        // Compute the new basis vectors
        double[] u = subtract(B, A);  // Vector from A to B
        double[] w = crossProduct(u, subtract(C, A));  // Orthogonal vector to the plane defined by A, B, and C
        double[] v = crossProduct(w, u);  // Vector orthogonal to both u and w

        // Normalize the basis vectors to form an orthonormal basis
        u = normalize(u);
        v = normalize(v);
        w = normalize(w);

        // Construct the rotation matrix from the old basis to the new basis
        double[][] rotationMatrix = {u, v, w};

        // Calculate the translation vector to shift origin to A
        double[] translationVector = new double[]{-dotProduct(rotationMatrix[0], A), 
                                                  -dotProduct(rotationMatrix[1], A), 
                                                  -dotProduct(rotationMatrix[2], A)};

        // Apply the rotation and translation to the point cloud
        double[][] transformedPointCloud = new double[pointCloud.length][3];
        for (int i = 0; i < pointCloud.length; i++) {
            double[] point = pointCloud[i];
            transformedPointCloud[i] = add(multiply(rotationMatrix, subtract(point, A)), translationVector);
        }

        return transformedPointCloud;
    }

    // Helper methods for vector operations
    private static double[] subtract(double[] a, double[] b) {
        return new double[]{a[0] - b[0], a[1] - b[1], a[2] - b[2]};
    }

    private static double[] add(double[] a, double[] b) {
        return new double[]{a[0] + b[0], a[1] + b[1], a[2] + b[2]};
    }

    private static double[] multiply(double[][] matrix, double[] vector) {
        double[] result = new double[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            result[i] = dotProduct(matrix[i], vector);
        }
        return result;
    }

    private static double[] normalize(double[] vector) {
        double norm = Math.sqrt(dotProduct(vector, vector));
        return new double[]{vector[0] / norm, vector[1] / norm, vector[2] / norm};
    }

    private static double dotProduct(double[] a, double[] b) {
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    }

    private static double[] crossProduct(double[] a, double[] b) {
        return new double[]{
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        };
    }
}
