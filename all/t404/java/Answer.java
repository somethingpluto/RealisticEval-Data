package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Computes the n-th power of a matrix using the fast exponentiation method.
     *
     * @param matrix A square matrix to be exponentiated.
     * @param n      The exponent to raise the matrix to. Must be a non-negative integer.
     * @return The matrix raised to the power of n.
     */
    public static List<List<Integer>> power(List<List<Integer>> matrix, int n) throws IllegalArgumentException {
        if (n < 0) {
            throw new IllegalArgumentException("The exponent must be a non-negative integer.");
        }

        // Initialize result as identity matrix
        int size = matrix.size();
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < size; j++) {
                if (i == j) {
                    row.add(1);
                } else {
                    row.add(0);
                }
            }
            result.add(row);
        }

        while (n > 0) {
            if ((n & 1) == 1) { // Check if n is odd
                result = multiplyMatrices(result, matrix);
            }
            matrix = multiplyMatrices(matrix, matrix); // Square the matrix
            n >>= 1; // Divide n by 2
        }

        return result;
    }

    private static List<List<Integer>> multiplyMatrices(List<List<Integer>> a, List<List<Integer>> b) {
        int size = a.size();
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < size; j++) {
                int sum = 0;
                for (int k = 0; k < size; k++) {
                    sum += a.get(i).get(k) * b.get(k).get(j);
                }
                row.add(sum);
            }
            result.add(row);
        }
        return result;
    }
}