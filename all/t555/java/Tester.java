package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import static org.real.temp.Answer.*;
public class Tester {

    private static final double DELTA = 1e-15;

    @Test
    public void testIdentityQuaternion() {
        double[] quaternion = {1.0, 0.0, 0.0, 0.0};
        double expectedAngle = 0.0;
        assertEquals(expectedAngle, quaternionToAngle(quaternion), DELTA);
    }

    @Test
    public void test180DegreesRotation() {
        double[] quaternion = {0.0, 0.0, 1.0, 0.0};  // 180 degrees around Z axis
        double expectedAngle = Math.PI;  // 180 degrees in radians
        assertEquals(expectedAngle, quaternionToAngle(quaternion), DELTA);
    }

    @Test
    public void test360DegreesRotation() {
        double[] quaternion = {1.0, 0.0, 0.0, 0.0};  // Full rotation
        double expectedAngle = 0.0;  // 360 degrees is equivalent to 0 degrees
        assertEquals(expectedAngle, quaternionToAngle(quaternion), DELTA);
    }

    @Test
    public void testNonUnitQuaternion() {
        double[] quaternion = {0.5, 0.5, 0.5, 0.5};  // This is not normalized
        // Normalize the quaternion first
        double norm = Math.sqrt(Arrays.stream(quaternion).map(x -> x * x).sum());
        double[] normalizedQuaternion = Arrays.stream(quaternion).map(x -> x / norm).toArray();
        double expectedAngle = 2 * Math.acos(normalizedQuaternion[0]);  // Should be same angle
        assertEquals(expectedAngle, quaternionToAngle(normalizedQuaternion), DELTA);
    }

    @Test
    public void testInvalidQuaternion() {
        assertThrows(IllegalArgumentException.class, () -> {
            quaternionToAngle(new double[]{1.0, 0.0, 0.0});  // Only 3 components
        });
    }
}