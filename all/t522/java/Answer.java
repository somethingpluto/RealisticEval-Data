package org.real.temp;

import org.ejml.simple.SimpleMatrix;

public class Answer {

    /**
     * Rotate the point cloud around the Y axis by a given angle.
     *
     * @param pointCloud A N x 3 matrix representing the 3D point cloud.
     * @param rotationAngle The angle (in radians) to rotate the point cloud.
     * @return A N x 3 matrix of the rotated point cloud.
     */
    public static SimpleMatrix rotatePointCloud(SimpleMatrix pointCloud, double rotationAngle) {
        // Create the rotation matrix for a rotation around the Y axis
        SimpleMatrix rotationMatrix = new SimpleMatrix(3, 3);
        rotationMatrix.set(0, 0, Math.cos(rotationAngle));
        rotationMatrix.set(0, 2, Math.sin(rotationAngle));
        rotationMatrix.set(2, 0, -Math.sin(rotationAngle));
        rotationMatrix.set(2, 2, Math.cos(rotationAngle));
        rotationMatrix.set(1, 1, 1);

        // Rotate the point cloud by multiplying with the rotation matrix
        SimpleMatrix rotatedPointCloud = pointCloud.mult(rotationMatrix);

        return rotatedPointCloud;
    }

    public static void main(String[] args) {
        // Example usage
        SimpleMatrix pointCloud = new SimpleMatrix(new double[][]{
            {1, 2, 3},
            {4, 5, 6}
        });

        double rotationAngle = Math.PI / 4; // 45 degrees in radians
        SimpleMatrix rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);
        System.out.println(rotatedPointCloud);
    }
}