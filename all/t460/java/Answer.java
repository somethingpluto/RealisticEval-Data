package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Double> matrixVectorMultiplication(List<List<Double>> matrix, List<Double> vector) throws IllegalArgumentException {
        // Check if the dimensions of the matrix and vector are compatible for multiplication
        if (matrix.get(0).size() != vector.size()) {
            throw new IllegalArgumentException("The number of columns in the matrix must be equal to the number of elements in the vector");
        }

        // Create a new list to store the result
        List<Double> result = new ArrayList<>();

        // Perform the multiplication
        for (int i = 0; i < matrix.size(); i++) {
            double sum = 0;
            for (int j = 0; j < matrix.get(i).size(); j++) {
                sum += matrix.get(i).get(j) * vector.get(j);
            }
            result.add(sum);
        }

        return result;
    }
}
