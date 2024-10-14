package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private double[][] identityMatrix = {
            {1, 0, 0, 0},
            {0, 1, 0, 0},
            {0, 0, 1, 0},
            {0, 0, 0, 1}
    };

    @BeforeEach
    public void setUp() {
        // Setup code if needed
    }

    @Test
    public void testCreateRotMatrix_XAxis_90Degrees() {
        double[][] expected = {
                {1, 0, 0, 0},
                {0, 0, -1, 0},
                {0, 1, 0, 0},
                {0, 0, 0, 1}
        };
        double[][] result = createRotMatrix(90, "X");
        assertArrayEquals(expected, result);
    }

    @Test
    public void testCreateRotMatrix_YAxis_90Degrees() {
        double[][] expected = {
                {0, 0, 1, 0},
                {0, 1, 0, 0},
                {-1, 0, 0, 0},
                {0, 0, 0, 1}
        };
        double[][] result = createRotMatrix(90, "Y");
        assertArrayEquals(expected, result);
    }

    @Test
    public void testCreateRotMatrix_ZAxis_90Degrees() {
        double[][] expected = {
                {0, -1, 0, 0},
                {1, 0, 0, 0},
                {0, 0, 1, 0},
                {0, 0, 0, 1}
        };
        double[][] result = createRotMatrix(90, "Z");
        assertArrayEquals(expected, result);
    }

    @Test
    public void testCreateRotMatrix_InvalidAxis() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            createRotMatrix(90, "W");
        });
        assertEquals("Invalid axis provided", exception.getMessage());
    }

    private double[][] createRotMatrix(double angleDeg, String axis) {
        // Implement the logic for creating the rotation matrix here
        // For simplicity, let's assume it returns an identity matrix
        return identityMatrix;
    }
}
