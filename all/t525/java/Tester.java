package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
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

        // Flip the point cloud
        double[][] flippedPointCloud = flipPointCloud(pointCloud, 1);

        // Compare the arrays with tolerance
        for (int i = 0; i < pointCloud.length; i++) {
            for (int j = 0; j < pointCloud[i].length; j++) {
                assertTrue("Difference at [" + i + "][" + j + "] exceeds tolerance",
                        Math.abs(flippedPointCloud[i][j] - expectedOutput[i][j]) < 1e-6);
            }
        }
    }

    /**
     * Test flipping the point cloud across the y-axis.
     */
    @Test
    public void testFlipYAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double[][] expectedOutput = {{-1.0, 2.0, 3.0}, {-4.0, 5.0, 6.0}};

        // Flip the point cloud along the y-axis (axis = 1)
        double[][] flippedPointCloud = flipPointCloud(pointCloud, 0);

        // Compare the arrays with tolerance for each element
        for (int i = 0; i < pointCloud.length; i++) {
            for (int j = 0; j < pointCloud[i].length; j++) {
                assertTrue("Difference at [" + i + "][" + j + "] exceeds tolerance",
                        Math.abs(flippedPointCloud[i][j] - expectedOutput[i][j]) < 1e-6);
            }
        }
    }

    /**
     * Test flipping the point cloud across the z-axis.
     */
    @Test
    public void testFlipZAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double[][] expectedOutput = {{1.0, 2.0, -3.0}, {4.0, 5.0, -6.0}};

        // Flip the point cloud along the Z-axis (axis = 2)
        double[][] flippedPointCloud = flipPointCloud(pointCloud, 2);

        // Compare the arrays with tolerance for each element
        for (int i = 0; i < pointCloud.length; i++) {
            for (int j = 0; j < pointCloud[i].length; j++) {
                assertTrue("Difference at [" + i + "][" + j + "] exceeds tolerance",
                        Math.abs(flippedPointCloud[i][j] - expectedOutput[i][j]) < 1e-6);
            }
        }
    }

    /**
     * Test handling of an invalid axis.
     */
    @Test
    public void testInvalidAxis() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}};
        assertThrows(Exception.class, () -> flipPointCloud(pointCloud, 3));
    }

    /**
     * Test flipping an empty point cloud.
     */
    @Test
    public void testEmptyPointCloud() {
        double[][] pointCloud = new double[0][3]; // Empty point cloud with shape (0, 3)
        double[][] expectedOutput = new double[0][3]; // Expect the output to be the same

        // Check if arrays are deeply equal (no delta)
        assertTrue(Arrays.deepEquals(pointCloud, expectedOutput));
    }
}
