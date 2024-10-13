package org.real.temp;

import java.util.*;

public class Answer {
    private static final int TOTAL_DRAWS = 15;

    /**
     * Calculate the probability that n red balls will be drawn when 15 balls are drawn with replacement
     * from a jar containing x red balls and y blue balls.
     *
     * @param n Number of red balls to be drawn.
     * @param x Number of red balls in the jar.
     * @param y Number of blue balls in the jar.
     * @return The probability of drawing exactly n red balls.
     */
    public static double probabilityOfRedBalls(int n, int x, int y) {
        double p = (double) x / (x + y); // Probability of drawing a red ball

        // Calculate the probability using the binomial formula
        double probability = comb(TOTAL_DRAWS, n) * Math.pow(p, n) * Math.pow(1 - p, TOTAL_DRAWS - n);
        return probability;
    }

    // Helper method to calculate combinations (n choose k)
    private static long comb(int n, int k) {
        long result = 1;
        for (int i = 0; i < k; i++) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }

    // Main method for testing
    public static void main(String[] args) {
        System.out.println(probabilityOfRedBalls(3, 7, 8)); // Example test case
    }
}