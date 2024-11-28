package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<List<Integer>> multiplyMatrices(List<List<Integer>> A, List<List<Integer>> B) {
        int rowsA = A.size();
        int colsA = A.get(0).size();
        int colsB = B.get(0).size();

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < rowsA; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < colsB; j++) {
                int sum = 0;
                for (int k = 0; k < colsA; k++) {
                    sum += A.get(i).get(k) * B.get(k).get(j);
                }
                row.add(sum);
            }
            result.add(row);
        }
        return result;
    }

    public static List<List<Integer>> power(List<List<Integer>> matrix, int n) throws IllegalArgumentException {
        if (n < 0) {
            throw new IllegalArgumentException("The exponent n must be a non-negative integer.");
        }

        // Identity matrix of the same size as the input matrix
        List<List<Integer>> result = new ArrayList<>();
        int size = matrix.size();
        for (int i = 0; i < size; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < size; j++) {
                row.add(i == j ? 1 : 0);
            }
            result.add(row);
        }

        List<List<Integer>> base = new ArrayList<>(matrix);

        while (n > 0) {
            if (n % 2 == 1) {
                result = multiplyMatrices(result, base);
            }
            base = multiplyMatrices(base, base);
            n /= 2;
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(List.of(1, 2)));
        matrix.add(new ArrayList<>(List.of(3, 4)));

        int n = 2;
        try {
            List<List<Integer>> result = power(matrix, n);
            System.out.println("Result: " + result);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}