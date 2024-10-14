import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

public class Tester {

    @Test
    public void testZeroRotation() {
        // Test with zero rotation for all axes
        double[][] R = eulerToRotationMatrix(0, 0, 0);
        double[][] expected = {
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        };
        assertArrayEquals(expected, R, 1e-6);
    }

    @Test
    public void testRotationAboutX() {
        // Test rotation about the x-axis
        double[][] R = eulerToRotationMatrix(90, 0, 0);
        double[][] expected = {
            {1, 0, 0},
            {0, 0, -1},
            {0, 1, 0}
        };
        assertArrayEquals(expected, R, 1e-6);
    }

    @Test
    public void testRotationAboutY() {
        // Test rotation about the y-axis
        double[][] R = eulerToRotationMatrix(90, 0, 0);
        double[][] expected = {
            {0, 0, 1},
            {0, 1, 0},
            {-1, 0, 0}
        };
        assertArrayEquals(expected, R, 1e-6);
    }

    @Test
    public void testRotationAboutZ() {
        // Test rotation about the z-axis
        double[][] R = eulerToRotationMatrix(0, 0, 90);
        double[][] expected = {
            {0, -1, 0},
            {1, 0, 0},
            {0, 0, 1}
        };
        assertArrayEquals(expected, R, 1e-6);
    }

    @Test
    public void testCombinedRotation() {
        // Test combined rotation
        double[][] R = eulerToRotationMatrix(30, 45, 60);
        double[][] expected = {
            {0.35355339, -0.5732233, 0.73919892},
            {0.61237244, 0.73919892, 0.28033009},
            {-0.70710678, 0.35355339, 0.61237244}
        };
        assertArrayEquals(expected, R, 1e-5);
    }
}