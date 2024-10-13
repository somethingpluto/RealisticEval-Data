package org.real.temp;

import java.math.BigInteger;

public class Answer {

    /**
     * Calculate the probability that x balls randomly drawn from a jar containing
     * n red balls and m blue balls will all be red balls.
     *
     * @param x Number of balls to draw.
     * @param n Number of red balls in the jar.
     * @param m Number of blue balls in the jar.
     * @return The probability that all x drawn balls are red.
     */
    public static double probabilityRedBalls(int x, int n, int m) {
        if (x > n) {
            return 0; // Not enough red balls to draw x red balls
        }
        int totalBalls = n + m;
        if (x > totalBalls) {
            return 0; // Not enough balls to draw x balls of any color
        }

        BigInteger waysToChooseRed = comb(n, x);
        BigInteger totalWaysToChooseBalls = comb(totalBalls, x);

        // Probability that all chosen balls are red
        double probability = waysToChooseRed.doubleValue() / totalWaysToChooseBalls.doubleValue();

        return probability;
    }

    /**
     * Calculates the number of combinations (n choose k).
     *
     * @param n The total number of items.
     * @param k The number of items to choose.
     * @return The number of combinations.
     */
    private static BigInteger comb(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for (int i = 0; i < k; i++) {
            result = result.multiply(BigInteger.valueOf(n - i))
                           .divide(BigInteger.valueOf(i + 1));
        }
        return result;
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(probabilityRedBalls(2, 5, 7)); // Example call to the method
    }
}