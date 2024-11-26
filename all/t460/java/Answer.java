package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Performs matrix-vector multiplication.
     * 
     * @param matrix The matrix represented as a list of lists of doubles.
     * @param vector The vector represented as a list of doubles.
     * @return The resulting vector after multiplication.
     * @throws IllegalArgumentException If the matrix and vector dimensions are not compatible.
     */
    public static List<Double> matrixVectorMultiplication(List<List<Double>> matrix, List<Double> vector) throws IllegalArgumentException {
        // Ensure matrix dimensions are compatible with vector length
        if (matrix.get(0).size() != vector.size()) {
            throw new IllegalArgumentException("Matrix and vector dimensions are not compatible for multiplication");
        }

        // Initialize the result list with zeros
        List<Double> result = new ArrayList<>(matrix.size());
        for (int i = 0; i < matrix.size(); i++) {
            result.add(0.0);
        }

        // Perform the matrix-vector multiplication
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < vector.size(); j++) {
                result.set(i, result.get(i) + matrix.get(i).get(j) * vector.get(j));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        List<List<Double>> matrix = new ArrayList<>();
        matrix.add(List.of(1.0, 2.0, 3.0));
        matrix.add(List.of(4.0, 5.0, 6.0));
        matrix.add(List.of(7.0, 8.0, 9.0));

        List<Double> vector = List.of(1.0, 0.0, 1.0);

        try {
            List<Double> result = matrixVectorMultiplication(matrix, vector);
            System.out.println(result);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}