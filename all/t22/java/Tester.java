package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class Tester {

    @Test
    public void testBasicFunctionality() {
        // Basic logic functionality test
        double[] point1 = {0.0, 0.0};
        double[] point2 = {3.0, 4.0};
        double expectedDistance = 5.0;
        assertEquals(expectedDistance, calculateEuclideanDistance(point1, point2), 0.001, "Should calculate the distance correctly");
    }

    @Test
    public void testNegativeCoordinates() {
        // Test with negative coordinates
        double[] point1 = {-1.0, -1.0};
        double[] point2 = {-4.0, -5.0};
        double expectedDistance = 5.0;
        assertEquals(expectedDistance, calculateEuclideanDistance(point1, point2), 0.001, "Should handle negative coordinates correctly");
    }

    @Test
    public void testZeroDistance() {
        // Boundary test: points are the same
        double[] point1 = {2.0, 3.0};
        double[] point2 = {2.0, 3.0};
        double expectedDistance = 0.0;
        assertEquals(expectedDistance, calculateEuclideanDistance(point1, point2), 0.001, "Should return 0 when both points are the same");
    }

    @Test
    public void testLargeCoordinates() {
        // Boundary test: large coordinates
        double[] point1 = {1e6, 1e6};
        double[] point2 = {1e6 + 3, 1e6 + 4};
        double expectedDistance = 5.0;
        assertEquals(expectedDistance, calculateEuclideanDistance(point1, point2), 0.001, "Should handle large coordinates correctly");
    }

    @Test
    public void testInvalidInput() {
        // Exception handling test: invalid input (null)
        assertThrows(IllegalArgumentException.class, () -> {
            calculateEuclideanDistance(null, new double[]{0.0, 0.0});
        });
    }
}
