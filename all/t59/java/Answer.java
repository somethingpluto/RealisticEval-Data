package org.real.temp;

public class Answer {
    /**
     * Calculate the probability that x balls will be randomly drawn from a jar
     * containing n red balls and m blue balls, and all of them will be red balls.
     *
     * @param x Number of balls to draw.
     * @param n Number of red balls in the jar.
     * @param m Number of blue balls in the jar.
     * @return The probability that all x drawn balls are red.
     */
    public static double probabilityRedBalls(int x, int n, int m) {
        if (x > n + m || x < 0) {
            return 0; // Invalid input
        }

        double numerator = factorial(n) / (factorial(x) * factorial(n - x));
        double denominator = factorial(n + m) / (factorial(m) * factorial(n));

        return numerator / denominator;
    }

    private static double factorial(int number) {
        if (number == 0)
            return 1;
        else {
            double result = 1;
            for (int factor = 2; factor <= number; ++factor) {
                result *= factor;
            }
            return result;
        }
    }
}