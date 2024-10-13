package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

public class Tester {

    private INDArray K;

    @Before
    public void setUp() {
        // Define a common intrinsic matrix for testing
        K = Nd4j.create(new double[][]{
            {1000, 0, 320},
            {0, 1000, 240},
            {0, 0, 1}
        });
    }

    @Test
    public void testCenterCoordinates() {
        // Test with center pixel coordinates where x and y should map to zero in NDC.
        double[] result = get3DCoordinates(K, 100, 320, 240);
        assertArrayEquals(new double[]{0.0, 0.0, 100}, result, 1e-6);
    }

    @Test
    public void testBoundaryCoordinates() {
        // Test with boundary values in the image frame.
        double[] result = get3DCoordinates(K, 50, 640, 480);
        double expectedX = (640 - 320) / 1000 * 50;
        double expectedY = (480 - 240) / 1000 * 50;
        assertArrayEquals(new double[]{expectedX, expectedY, 50}, result, 1e-6);
    }

    @Test
    public void testNegativeDepth() {
        // Test with a negative depth to see if it handles incorrect input properly.
        double[] result = get3DCoordinates(K, -100, 320, 240);
        assertArrayEquals(new double[]{0.0, 0.0, -100}, result, 1e-6);
    }

    @Test
    public void testZeroDepth() {
        // Test with zero depth which should lead to a zero-length vector.
        double[] result = get3DCoordinates(K, 0, 320, 240);
        assertArrayEquals(new double[]{0.0, 0.0, 0.0}, result, 1e-6);
    }

    @Test
    public void testNonIntegerValues() {
        // Test with non-integer pixel coordinates.
        double[] result = get3DCoordinates(K, 100, 320.5, 240.5);
        double expectedX = (320.5 - 320) / 1000 * 100;
        double expectedY = (240.5 - 240) / 1000 * 100;
        assertArrayEquals(new double[]{expectedX, expectedY, 100}, result, 1e-6);
    }
}