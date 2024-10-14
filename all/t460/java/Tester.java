package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;

public class Tester {

    public List<Double> matrixVectorMultiplication(List<List<Double>> matrix, List<Double> vector) {
        if (matrix.get(0).size() != vector.size()) {
            throw new IllegalArgumentException("Matrix and vector dimensions are not compatible for multiplication.");
        }

        List<Double> result = new ArrayList<>();
        for (List<Double> row : matrix) {
            double sum = 0;
            for (int i = 0; i < row.size(); i++) {
                sum += row.get(i) * vector.get(i);
            }
            result.add(sum);
        }
        return result;
    }

    @Test
    public void testValidMatrixVectorMultiplication() {
        List<List<Double>> matrix = Arrays.asList(
            Arrays.asList(1.0, 2.0),
            Arrays.asList(3.0, 4.0)
        );
        List<Double> vector = Arrays.asList(5.0, 6.0);
        List<Double> expectedResult = Arrays.asList(17.0, 39.0);
        assertEquals(expectedResult, matrixVectorMultiplication(matrix, vector));
    }

    @Test
    public void testInvalidMatrixVectorMultiplication() {
        List<List<Double>> matrix = Arrays.asList(
            Arrays.asList(1.0, 2.0),
            Arrays.asList(3.0, 4.0)
        );
        List<Double> vector = Arrays.asList(5.0);
        assertThrows(IllegalArgumentException.class, () -> matrixVectorMultiplication(matrix, vector));
    }
}