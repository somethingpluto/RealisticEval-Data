package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the getRotation function.
 */
public class Tester {

    /**
     * Test for a rotation of 0 degrees (identity matrix).
     */
    @Test
    public void testRotation0Degrees() {
        double[][] matrix = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0}
        };
        double expectedRotation = 0.0;
        assertEquals(expectedRotation, getRotation(matrix), 1e-6);
    }

    /**
     * Test for a rotation of 90 degrees.
     */
    @Test
    public void testRotation90Degrees() {
        double[][] matrix = {
            {0.0, -1.0, 0.0},
            {1.0, 0.0, 0.0},
            {0.0, 0.0, 1.0}
        };
        double expectedRotation = Math.PI / 2;  // 90 degrees in radians
        assertEquals(expectedRotation, getRotation(matrix), 1e-6);
    }

    /**
     * Test for a rotation of 180 degrees.
     */
    @Test
    public void testRotation180Degrees() {
        double[][] matrix = {
            {-1.0, 0.0, 0.0},
            {0.0, -1.0, 0.0},
            {0.0, 0.0, 1.0}
        };
        double expectedRotation = Math.PI;  // 180 degrees in radians
        assertEquals(expectedRotation, getRotation(matrix), 1e-6);
    }

    /**
     * Test for a rotation of -90 degrees.
     */
    @Test
    public void testRotationNegative90Degrees() {
        double[][] matrix = {
            {0.0, 1.0, 0.0},
            {-1.0, 0.0, 0.0},
            {0.0, 0.0, 1.0}
        };
        double expectedRotation = -Math.PI / 2;  // -90 degrees in radians
        assertEquals(expectedRotation, getRotation(matrix), 1e-6);
    }

}