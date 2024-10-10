import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testProbabilityRedBalls() {
        // Arrange
        int x = 3;
        int n = 5;
        int m = 7;
        double expectedProbability = calculateExpectedProbability(x, n, m);

        // Act
        double actualProbability = probabilityRedBalls(x, n, m);

        // Assert
        assertEquals(expectedProbability, actualProbability, 0.001);
    }

    private double calculateExpectedProbability(int x, int n, int m) {
        // Calculate the expected probability based on the formula
        return Math.pow(n / (double)(n + m), x);
    }

    private double probabilityRedBalls(int x, int n, int m) {
        // Implement the logic for calculating the probability
        if (x > n || x < 0) {
            throw new IllegalArgumentException("Invalid number of balls to draw");
        }

        long numerator = factorial(n) / (factorial(x) * factorial(n - x));
        long denominator = factorial(m + n) / (factorial(m) * factorial(n));

        return (double)numerator / denominator;
    }

    private long factorial(int num) {
        if (num == 0 || num == 1) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }
}