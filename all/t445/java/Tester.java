package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import static org.real.temp.Answer.*;
/**
 * Test class for the createRotMatrix method.
 */
public class Tester {

    /**
     * Test rotation around the X-axis for 90 degrees.
     */
    @Test
    public void testRotationX90Degrees() {
        double[][] expectedMatrix = {
            {1, 0, 0, 0},
            {0, 0, -1, 0},
            {0, 1, 0, 0},
            {0, 0, 0, 1}
        };
        double[][] resultMatrix = createRotMatrix(90, "x");
        assertArrayEquals(expectedMatrix, resultMatrix, 1e-6);
    }

    /**
     * Test rotation around the Y-axis for 180 degrees.
     */
    @Test
    public void testRotationY180Degrees() {
        double[][] expectedMatrix = {
            {-1, 0, 0, 0},
            {0, 1, 0, 0},
            {0, 0, -1, 0},
            {0, 0, 0, 1}
        };
        double[][] resultMatrix = createRotMatrix(180, "y");
        assertArrayEquals(expectedMatrix, resultMatrix, 1e-6);
    }

    /**
     * Test rotation around the Z-axis for 270 degrees (or -90 degrees).
     */
    @Test
    public void testRotationZ270Degrees() {
        double[][] expectedMatrix = {
            {0, 1, 0, 0},
            {-1, 0, 0, 0},
            {0, 0, 1, 0},
            {0, 0, 0, 1}
        };
        double[][] resultMatrix = createRotMatrix(270, "z");
        assertArrayEquals(expectedMatrix, resultMatrix, 1e-6);
    }

    /**
     * Test behavior with invalid axis input.
     */
    @Test
    public void testInvalidAxis() {
        assertThrows(IllegalArgumentException.class, () -> {
            createRotMatrix(90, "a");
        });
    }

    /**
     * Test zero degree rotation which should lead to the identity matrix.
     */
    @Test
    public void testZeroRotation() {
        double[][] expectedMatrix = {
            {1, 0, 0, 0},
            {0, 1, 0, 0},
            {0, 0, 1, 0},
            {0, 0, 0, 1}
        };
        double[][] resultMatrix = createRotMatrix(0, "x");
        assertArrayEquals(expectedMatrix, resultMatrix, 1e-6);
    }

    // Helper method to compare arrays with a tolerance
    private static void assertArrayEquals(double[][] expected, double[][] actual, double delta) {
        assertEquals(expected.length, actual.length);
        for (int i = 0; i < expected.length; i++) {
            assertEquals(expected[i].length, actual[i].length);
            for (int j = 0; j < expected[i].length; j++) {
                assertEquals(expected[i][j], actual[i][j], delta);
            }
        }
    }
}