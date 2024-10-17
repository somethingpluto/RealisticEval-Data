package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

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

        assertArrayEquals(expectedOutput, scaledPointCloud, 0.001);
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

        assertArrayEquals(expectedOutput, scaledPointCloud, 0.001);
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

        assertArrayEquals(expectedOutput, scaledPointCloud, 0.001);
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

        assertArrayEquals(expectedOutput, scaledPointCloud, 0.001);
    }

    // Utility method to scale the point cloud
    private double[][] scalePointCloud(double[][] pointCloud, double scaleFactor) {
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
}