package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    @Test
    public void testZeroRotation() {
        // Test when the original and target vectors are the same
        Vec3 original = new Vec3(1, 0, 0);
        Vec3 target = new Vec3(1, 0, 0);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // Expecting an identity matrix for no rotation
        double[][] expected = {
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        };

        assertArrayEquals(expected, result);
    }

    @Test
    public void test90DegreeRotation() {
        // Test for a 90 degree rotation around the Z-axis (from X to Y)
        Vec3 original = new Vec3(1, 0, 0);
        Vec3 target = new Vec3(0, 1, 0);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // Expected 90-degree rotation matrix around the Z-axis
        double[][] expected = {
            {0, -1, 0},
            {1, 0, 0},
            {0, 0, 1}
        };

        assertArrayEquals(expected, result);
    }

    @Test
    public void test180DegreeRotation() {
        // Test for a 180 degree rotation (opposite direction)
        Vec3 original = new Vec3(1, 0, 0);
        Vec3 target = new Vec3(-1, 0, 0);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // Expected 180-degree rotation matrix around the Z-axis
        double[][] expected = {
            {-1, 0, 0},
            {0, -1, 0},
            {0, 0, 1}
        };

        assertArrayEquals(expected, result);
    }

    @Test
    public void testArbitraryRotation() {
        // Test for an arbitrary rotation
        Vec3 original = new Vec3(1, 0, 0);
        Vec3 target = new Vec3(0, 0, 1);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // The expected rotation matrix should rotate from X-axis to Z-axis
        double[][] expected = {
            {0, 0, 1},
            {0, 1, 0},
            {-1, 0, 0}
        };

        assertArrayEquals(expected, result);
    }

    @Test
    public void testNonOrthogonalRotation() {
        // Test for a non-orthogonal vector rotation
        Vec3 original = new Vec3(1, 1, 0);
        Vec3 target = new Vec3(0, 1, 1);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // Since the vectors aren't aligned to a single axis, we won't use exact values.
        // Instead, we verify the structure of the result matrix.
        assertNotNull(result);
        assertEquals(3, result.length);  // 3x3 matrix
        assertEquals(3, result[0].length);
    }

    @Test
    public void testDifferentLengthVectors() {
        // Test when vectors have different lengths
        Vec3 original = new Vec3(2, 0, 0);
        Vec3 target = new Vec3(0, 3, 0);

        double[][] result = Answer.calculateRotationMatrix(original, target);

        // Expected 90-degree rotation matrix around the Z-axis
        double[][] expected = {
            {0, -1, 0},
            {1, 0, 0},
            {0, 0, 1}
        };

        assertArrayEquals(expected, result);
    }
}