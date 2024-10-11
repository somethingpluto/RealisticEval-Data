package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testSpiralTraversal() {
        MatrixTraversal traversal = new MatrixTraversal();

        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        assertEquals(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5), traversal.spiralTraversal(matrix1));

        int[][] matrix2 = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };
        assertEquals(List.of(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7), traversal.spiralTraversal(matrix2));

        int[][] matrix3 = {
            {1}
        };
        assertEquals(List.of(1), traversal.spiralTraversal(matrix3));

        int[][] matrix4 = {};
        assertEquals(List.of(), traversal.spiralTraversal(matrix4));
    }
}