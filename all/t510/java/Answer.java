package org.real.temp;

public class Answer {

    /**
     * Find the powers of 2 and 3 that multiply to produce the given number.
     *
     * @param num A positive integer greater than zero.
     * @return A pair (n, m) where n is the power of 2 and m is the power of 3.
     *         Returns null if the number is zero or if the number has prime factors other than 2 and 3.
     */
    public static Integer[] findPowers(int num) {
        // Input validation
        if (num <= 0) {
            throw new IllegalArgumentException("Input must be a positive integer greater than zero.");
        }

        int n = 0; // Initialize counter for powers of 2
        int m = 0; // Initialize counter for powers of 3

        // Count the power of 2 in the factorization
        while (num % 2 == 0) {
            n++;
            num /= 2;
        }

        // Count the power of 3 in the factorization
        while (num % 3 == 0) {
            m++;
            num /= 3;
        }

        // If num is reduced to 1, only 2's and 3's were factors
        if (num == 1) {
            return new Integer[]{n, m};
        } else {
            return null; // Return null if there are other prime factors
        }
    }

    public static void main(String[] args) {
        // Example usage
        Integer[] result = findPowers(72);
        if (result != null) {
            System.out.println("Powers: " + result[0] + ", " + result[1]);
        } else {
            System.out.println("The number has prime factors other than 2 and 3.");
        }
    }
}