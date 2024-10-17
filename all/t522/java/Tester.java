package org.real.temp;

import org.ejml.simple.SimpleMatrix;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for rotating a 3D point cloud.
 */
public class Tester {

    private static final double DELTA = 1e-6;

    /**
     * Test when the rotation angle is 0 (should return the same point cloud).
     */
    @Test
    public void testNoRotation() {
        SimpleMatrix pointCloud = new SimpleMatrix(new double[][]{{1.0, 2.0, 3.0}});
        double rotationAngle = 0;
        SimpleMatrix expectedOutput = pointCloud;

        SimpleMatrix rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        assertEquals(expectedOutput, rotatedPointCloud, DELTA);
    }

    /**
     * Test rotation of 180 degrees (π radians) around the Y axis.
     */
    @Test
    public void test180DegreeRotation() {
        SimpleMatrix pointCloud = new SimpleMatrix(new double[][]{{1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}});
        double rotationAngle = Math.PI; // 180 degrees
        SimpleMatrix expectedOutput = new SimpleMatrix(new double[][]{{-1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}});

        SimpleMatrix rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        assertEquals(expectedOutput, rotatedPointCloud, DELTA);
    }

    /**
     * Test rotation of 360 degrees (2π radians) around the Y axis (should return the same point cloud).
     */
    @Test
    public void testFullRotation() {
        SimpleMatrix pointCloud = new SimpleMatrix(new double[][]{{1.0, 2.0, 3.0}});
        double rotationAngle = 2 * Math.PI; // 360 degrees
        SimpleMatrix expectedOutput = pointCloud;

        SimpleMatrix rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        assertEquals(expectedOutput, rotatedPointCloud, DELTA);
    }

    /**
     * Helper method to rotate the point cloud.
     *
     * @param pointCloud A N x 3 matrix representing the 3D point cloud.
     * @param rotationAngle The angle (in radians) to rotate the point cloud.
     * @return A N x 3 matrix of the rotated point cloud.
     */
    private SimpleMatrix rotatePointCloud(SimpleMatrix pointCloud, double rotationAngle) {
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
}