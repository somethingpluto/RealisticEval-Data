package org.real.temp;

import org.junit.jupiter.api.Test; // JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertTrue; // JUnit 5 assertion method
import static org.junit.jupiter.api.Assertions.assertEquals; // JUnit 5 assertion method
import static org.junit.jupiter.api.Assertions.fail; // JUnit 5 fail method


public class Tester {

    private static final double DELTA = 1e-15;

    /**
     * Test the probability of drawing half red balls.
     */
    @Test
    public void testHalfRedBalls() {
        // Scenario where half of the drawn balls are expected to be red
        double result = probabilityOfRedBalls(7, 10, 10);
        double expectedResult = 0.001376; // Replace with the actual expected result
        assertTrue("Test with half red balls failed", isClose(result, expectedResult, DELTA));
    }

    /**
     * Test the probability of drawing some red balls.
     */
    @Test
    public void testSomeRedBalls() {
        // Scenario with some red balls in the jar, expecting a few red draws
        double result = probabilityOfRedBalls(5, 5, 10);
        double expectedResult = 0.02795; // Replace with the actual expected result
        assertTrue("Test with some red balls failed", isClose(result, expectedResult, DELTA));
    }

    /**
     * Test the probability of drawing red balls in an extreme case.
     */
    @Test
    public void testExtremeCase() {
        // Extreme scenario where the probability is low for the chosen n
        double result = probabilityOfRedBalls(15, 1, 99);
        double expectedResult = 0.000001; // Replace with the actual expected result
        assertTrue("Test with extreme case failed", isClose(result, expectedResult, DELTA));
    }

    // Helper method to check if two doubles are close enough
    private boolean isClose(double a, double b, double delta) {
        return Math.abs(a - b) <= delta;
    }
}