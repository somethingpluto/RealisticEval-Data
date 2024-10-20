package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testSpiralOrder() {
        MatrixSpiral matrixSpiral = new MatrixSpiral();

        // Test case 1
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        List<Integer> expected1 = Arrays.asList(1, 2, 3, 6, 9, 8, 7, 4, 5);
        assertEquals(expected1, matrixSpiral.spiralOrder(matrix1));

        // Test case 2
        int[][] matrix2 = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };
        List<Integer> expected2 = Arrays.asList(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7);
        assertEquals(expected2, matrixSpiral.spiralOrder(matrix2));

        // Test case 3
        int[][] matrix3 = {};
        List<Integer> expected3 = Arrays.asList();
        assertEquals(expected3, matrixSpiral.spiralOrder(matrix3));

        // Test case 4
        int[][] matrix4 = {{1}};
        List<Integer> expected4 = Arrays.asList(1);
        assertEquals(expected4, matrixSpiral.spiralOrder(matrix4));

        // Test case 5
        int[][] matrix5 = {
            {1, 2},
            {3, 4},
            {5, 6}
        };
        List<Integer> expected5 = Arrays.asList(1, 2, 4, 6, 5, 3);
        assertEquals(expected5, matrixSpiral.spiralOrder(matrix5));
    }
}

class MatrixSpiral {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) {
            return result;
        }

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right along the top row
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            // Traverse downwards along the right column
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            // Traverse from right to left along the bottom row, if still within bounds
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }

            // Traverse upwards along the left column, if still within bounds
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }
}
