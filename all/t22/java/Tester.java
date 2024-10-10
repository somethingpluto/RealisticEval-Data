import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testCalculateEuclideanDistance() {
        // Test data
        double[] point1 = {1.0, 2.0};
        double[] point2 = {4.0, 6.0};

        // Expected result
        double expectedResult = 5.0;

        // Actual result
        double actualResult = calculateEuclideanDistance(point1, point2);

        // Asserting the expected and actual results
        assertEquals(expectedResult, actualResult, 0.0);
    }

    private double calculateEuclideanDistance(double[] point1, double[] point2) {
        return Math.sqrt(Math.pow(point2[0] - point1[0], 2) + Math.pow(point2[1] - point1[1], 2));
    }
}