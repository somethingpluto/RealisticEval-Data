package org.real.temp;

public class Answer {
    /**
     * Find the largest integer between a given number n and half of it that is divisible by 10 or 5.
     *
     * @param n The upper bound of the range.
     * @return The largest integer between n and half of n that is divisible by 5,
     *         or null if no such number exists.
     */
    public static Integer findLargestDivisible(int n) {
        // Calculate half of n
        int halfN = n / 2;

        // Start checking from n down to halfN + 1
        for (int i = n; i >= halfN + 1; i--) {
            if (i % 10 == 0 || i % 5 == 0) {
                return i;
            }
        }

        // Return null if no such number exists
        return null;
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(findLargestDivisible(20)); // Output should be 20
        System.out.println(findLargestDivisible(9));  // Output should be 5
        System.out.println(findLargestDivisible(4));  // Output should be null
    }
}