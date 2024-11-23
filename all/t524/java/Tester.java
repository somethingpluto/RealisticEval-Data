package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertTrue;
import static org.real.temp.Answer.*;
/**
 * Test class for scaling a 3D point cloud.
 */
public class Tester {

    /**
     * Tests scaling of a single point.
     */
    @Test
    public void testSimpleScaling() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}};
        double scaleFactor = 2.0;
        double[][] expectedOutput = {{2.0, 4.0, 6.0}};

        double[][] scaledPointCloud = scalePointCloud(pointCloud, scaleFactor);

        // Use Arrays.deepEquals to compare two-dimensional arrays
        assertTrue(Arrays.deepEquals(expectedOutput, scaledPointCloud));
    }

    /**
     * Tests scaling of multiple points.
     */
    @Test
    public void testMultiplePointsScaling() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double scaleFactor = 0.5;
        double[][] expectedOutput = {{0.5, 1.0, 1.5}, {2.0, 2.5, 3.0}};

        double[][] scaledPointCloud = scalePointCloud(pointCloud, scaleFactor);

        assertTrue(Arrays.deepEquals(expectedOutput, scaledPointCloud));
    }

    /**
     * Tests scaling by a factor of zero (should return a point cloud of zeros).
     */
    @Test
    public void testZeroScaling() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        double scaleFactor = 0.0;
        double[][] expectedOutput = {{0.0, 0.0, 0.0}, {0.0, 0.0, 0.0}};

        double[][] scaledPointCloud = scalePointCloud(pointCloud, scaleFactor);

        assertTrue(Arrays.deepEquals(expectedOutput, scaledPointCloud));
    }

    /**
     * Tests scaling with a negative factor.
     */
    @Test
    public void testNegativeScaling() {
        double[][] pointCloud = {{1.0, 2.0, 3.0}};
        double scaleFactor = -2.0;
        double[][] expectedOutput = {{-2.0, -4.0, -6.0}};

        double[][] scaledPointCloud = scalePointCloud(pointCloud, scaleFactor);

        assertTrue(Arrays.deepEquals(expectedOutput, scaledPointCloud));
    }
}