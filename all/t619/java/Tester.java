package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testMultiplyMatrices_ValidInput() {
        double[][] matrixA = {
            {1, 2, 3},
            {4, 5, 6}
        };
        double[][] matrixB = {
            {7, 8},
            {9, 10},
            {11, 12}
        };
        double[][] expected = {
            {58, 64},
            {139, 154}
        };

        double[][] result = Answer.multiplyMatrix(matrixA, matrixB);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testMultiplyMatrices_ZeroMatrix() {
        double[][] matrixA = {
            {0, 0},
            {0, 0}
        };
        double[][] matrixB = {
            {1, 2},
            {3, 4}
        };
        double[][] expected = {
            {0, 0},
            {0, 0}
        };

        double[][] result = Answer.multiplyMatrix(matrixA, matrixB);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testMultiplyMatrices_SingleElement() {
        double[][] matrixA = {
            {5}
        };
        double[][] matrixB = {
            {3}
        };
        double[][] expected = {
            {15}
        };

        double[][] result = Answer.multiplyMatrix(matrixA, matrixB);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testMultiplyMatrices_IdentityMatrix() {
        double[][] matrixA = {
            {1, 2},
            {3, 4}
        };
        double[][] matrixB = {
            {1, 0},
            {0, 1}
        };
        double[][] expected = {
            {1, 2},
            {3, 4}
        };

        double[][] result = Answer.multiplyMatrix(matrixA, matrixB);
        assertArrayEquals(expected, result);
    }


    @Test
    public void testMultiplyMatrices_NegativeValues() {
        double[][] matrixA = {
            {-1, -2, -3},
            {-4, -5, -6}
        };
        double[][] matrixB = {
            {7, 8},
            {9, 10},
            {11, 12}
        };
        double[][] expected = {
            {-58, -64},
            {-139, -154}
        };

        double[][] result = Answer.multiplyMatrix(matrixA, matrixB);
        assertArrayEquals(expected, result);
    }
}
