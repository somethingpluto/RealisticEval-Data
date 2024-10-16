package org.real.temp;

import java.util.List;
import java.util.ArrayList;

public class Answer {
    public static List<List<Integer>> matrixMultiply(List<List<Integer>> matrixA, List<List<Integer>> matrixB) {
        // Check for null or empty matrices
        if (matrixA == null || matrixB == null || matrixA.isEmpty() || matrixB.isEmpty() || matrixA.get(0).isEmpty() || matrixB.get(0).isEmpty()) {
            return new ArrayList<>();
        }
        
        // Ensure matrix dimensions are compatible for multiplication
        if (matrixA.get(0).size() != matrixB.size()) {
            throw new IllegalArgumentException(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
        }

        // Initialize the result matrix with zeros
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < matrixA.size(); i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < matrixB.get(0).size(); j++) {
                row.add(0);
            }
            result.add(row);
        }

        // Perform matrix multiplication
        for (int i = 0; i < matrixA.size(); i++) {
            for (int j = 0; j < matrixB.get(0).size(); j++) {
                for (int k = 0; k < matrixB.size(); k++) {
                    result.get(i).set(j, result.get(i).get(j) + matrixA.get(i).get(k) * matrixB.get(k).get(j));
                }
            }
        }

        return result;
    }
}