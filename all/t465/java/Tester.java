package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for matrix-vector multiplication.
 */
public class Tester {

    private static final double[] ZERO_VECTOR = {0, 0};
    private static final double[] EXPECTED_RESULT_1 = {17, 39};
    private static final double[] EXPECTED_RESULT_2 = {13, 14, 7};
    private static final double[] EXPECTED_RESULT_3 = {0, 0};
    private static final double[] EXPECTED_RESULT_4 = {-3, -7};
    private static final double[] EXPECTED_RESULT_5 = {4, 10};

    @Test
    public void testCase1() {
        // Test with a simple 2x2 matrix and a 2-element vector
        double[][] matrix = {{1, 2}, {3, 4}};
        double[] vector = {5, 6};
        double[] expectedResult = EXPECTED_RESULT_1;

        double[] result = matrixVectorMultiplication(matrix, vector);
        assertArrayEquals(expectedResult, result, 0.0);
    }

    @Test
    public void testCase2() {
        // Test with a 3x3 matrix and a 3-element vector
        double[][] matrix = {{1, 0, 2}, {0, 1, 2}, {1, 1, 0}};
        double[] vector = {3, 4, 5};
        double[] expectedResult = EXPECTED_RESULT_2;

        double[] result = matrixVectorMultiplication(matrix, vector);
        assertArrayEquals(expectedResult, result, 0.0);
    }

    @Test
    public void testCase3() {
        // Test with a zero matrix and a vector
        double[][] matrix = {{0, 0}, {0, 0}};
        double[] vector = {1, 1};
        double[] expectedResult = ZERO_VECTOR;

        double[] result = matrixVectorMultiplication(matrix, vector);
        assertArrayEquals(expectedResult, result, 0.0);
    }

    @Test
    public void testCase4() {
        // Test with a matrix having negative values
        double[][] matrix = {{-1, -2}, {-3, -4}};
        double[] vector = {1, 1};
        double[] expectedResult = EXPECTED_RESULT_4;

        double[] result = matrixVectorMultiplication(matrix, vector);
        assertArrayEquals(expectedResult, result, 0.0);
    }

    @Test
    public void testCase5() {
        // Test with non-square matrix (2x3) and a compatible vector (3-element)
        double[][] matrix = {{1, 2, 3}, {4, 5, 6}};
        double[] vector = {1, 0, 1};
        double[] expectedResult = EXPECTED_RESULT_5;

        double[] result = matrixVectorMultiplication(matrix, vector);
        assertArrayEquals(expectedResult, result, 0.0);
    }

}