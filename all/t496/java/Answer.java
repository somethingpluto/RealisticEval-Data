package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Generates the ith row of Pascal's Triangle.
     *
     * @param i Row index (0-indexed)
     * @return A List representing the ith row of Pascal's Triangle
     */
    public static List<Long> pascalTriangleRow(int i) {
        List<Long> row = new ArrayList<>();
        for (int k = 0; k <= i; k++) {
            row.add(combination(i, k));
        }
        return row;
    }

    /**
     * Calculates the combination (n choose k).
     *
     * @param n The total number of items.
     * @param k The number of items to choose.
     * @return The combination value.
     */
    private static long combination(int n, int k) {
        long result = 1;
        if (k > n - k) {
            k = n - k;
        }
        for (int i = 0; i < k; ++i) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }

    // Example usage
    public static void main(String[] args) {
        List<Long> row = pascalTriangleRow(5);
        System.out.println(row); // Output: [1, 5, 10, 10, 5, 1]
    }
}