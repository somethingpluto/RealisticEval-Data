package org.real.temp;

public class Answer {

    /**
     * Find the largest integer between n and half of n that is divisible by 5.
     *
     * @param n The upper bound of the range.
     * @return The largest integer between n and half of n that is divisible by 5,
     *         or null if no such number exists.
     */
    public static Integer findLargestDivisible(int n) {
        // Start checking from n and go down to half of n
        int start = n;
        int end = n / 2;

        for (int i = start; i > end; i--) {
            if (i % 5 == 0) {
                return i;
            }
        }

        return null;  // Return null if no number divisible by 5 is found
    }

    public static void main(String[] args) {
        // Example usage
        int n = 20;
        Integer result = findLargestDivisible(n);
        System.out.println("The largest integer divisible by 5 between " + n + " and half of " + n + " is: " + result);
    }
}