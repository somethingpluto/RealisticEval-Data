package org.real.temp;

import org.junit.Before;
import org.junit.jupiter.api.Test;


import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;

public class Tester {

    private double[][] pointCloud;
    private double[][] refFramePoints;

    @Before
    public void setUp() {
        // Basic setup for tests, initialize some common point clouds and frames
        pointCloud = new double[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        refFramePoints = new double[][]{{0, 0, 0}, {1, 0, 0}, {0, 1, 0}};
    }

    @Test
    public void testIdentityTransformation() {
        // Test with an identity transformation where the reference frame is the standard basis
        double[][] result = transformPointCloudToReferenceFrame(pointCloud, refFramePoints);
        double[][] expected = new double[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        assertArrayEquals(expected, result);
    }

    @Test
    public void testTranslation() {
        // Only translation no rotation; move the origin
        double[][] framePoints = new double[][]{{1, 1, 1}, {2, 1, 1}, {1, 2, 1}};
        double[][] result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        double[][] expected = new double[][]{{-1, 0, 1}, {2, 3, 4}, {5, 6, 7}};
        assertArrayEquals(expected, result);
    }

    @Test
    public void testRotation() {
        // Rotation about z-axis by 90 degrees
        double[][] framePoints = new double[][]{{0, 0, 0}, {0, 1, 0}, {0, 1, 1}};
        double[][] result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        double[][] expected = new double[][]{{2, 3, 1}, {5, 6, 4}, {8, 9, 7}};
        assertArrayEquals(expected, result);
    }

    @Test
    public void testNonOrthonormalFrame() {
        // Use non-orthonormal frame to see how function handles it (should normalize internally)
        double[][] framePoints = new double[][]{{0, 0, 0}, {1, 0, 0}, {1, 1, 0}};
        double[][] result = transformPointCloudToReferenceFrame(pointCloud, framePoints);

        // Manually compute expected result
        double[] u = new double[]{1, 0, 0};
        double[] v = new double[]{0, 1, 0};
        double[] w = crossProduct(u, v);
        double[][] rotationMatrix = new double[][]{u, v, w};
        double[][] expected = matrixMultiply(pointCloud, transpose(rotationMatrix));

        assertArrayEquals(expected, result);
    }

    @Test
    public void testInvertedFrame() {
        // Inverting the frame to see if negatives are handled
        double[][] framePoints = new double[][]{{0, 0, 0}, {-1, 0, 0}, {0, -1, 0}};
        double[][] result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        double[][] expected = matrixMultiply(pointCloud, new double[][]{{-1, 0, 0}, {0, -1, 0}, {0, 0, 1}});

        assertArrayEquals(expected, result);
    }

    private double[] crossProduct(double[] a, double[] b) {
        return new double[]{
                a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0]
        };
    }

    private double[][] transpose(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] transposed = new double[cols][rows];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transposed[j][i] = matrix[i][j];
            }
        }
        return transposed;
    }

    private double[][] matrixMultiply(double[][] a, double[][] b) {
        // Check if the number of columns in a equals the number of rows in b
        if (a[0].length != b.length) {
            throw new IllegalArgumentException("Matrix A columns must match Matrix B rows.");
        }

        // Initialize the result matrix with the correct dimensions
        double[][] result = new double[a.length][b[0].length];

        // Perform matrix multiplication
        for (int i = 0; i < a.length; i++) { // Iterate over rows of A
            for (int j = 0; j < b[0].length; j++) { // Iterate over columns of B
                for (int k = 0; k < a[0].length; k++) { // Iterate over columns of A
                    result[i][j] += a[i][k] * b[k][j]; // Calculate the dot product
                }
            }
        }

        return result; // Return the resulting matrix
    }
}
