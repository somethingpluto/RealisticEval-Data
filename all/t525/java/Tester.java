package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertThrows;

/**
 * Test class for verifying the correctness of the flipPointCloud method.
 */
public class Tester {

    /**
     * Test flipping the point cloud across the x-axis.
     */
    @Test
    public void testFlipXAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double[][] expectedOutput = {{1.0, -2.0, 3.0}, {4.0, -5.0, 6.0}};
        assertArrayEquals(expectedOutput, flipPointCloud(pointCloud, 1), 1e-6);
    }

    /**
     * Test flipping the point cloud across the y-axis.
     */
    @Test
    public void testFlipYAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double[][] expectedOutput = {{-1.0, 2.0, 3.0}, {-4.0, 5.0, 6.0}};
        assertArrayEquals(expectedOutput, flipPointCloud(pointCloud, 0), 1e-6);
    }

    /**
     * Test flipping the point cloud across the z-axis.
     */
    @Test
    public void testFlipZAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double[][] expectedOutput = {{1.0, 2.0, -3.0}, {4.0, 5.0, -6.0}};
        assertArrayEquals(expectedOutput, flipPointCloud(pointCloud, 2), 1e-6);
    }

    /**
     * Test handling of an invalid axis.
     */
    @Test
    public void testInvalidAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}};
        assertThrows(IllegalArgumentException.class, () -> flipPointCloud(pointCloud, 3));
    }

    /**
     * Test flipping an empty point cloud.
     */
    @Test
    public void testEmptyPointCloud() {
        double[][] pointCloud = new double[0][3]; // Empty point cloud with shape (0, 3)
        double[][] expectedOutput = new double[0][3]; // Expect the output to be the same
        assertArrayEquals(expectedOutput, flipPointCloud(pointCloud, 0), 1e-6);
    }
}
