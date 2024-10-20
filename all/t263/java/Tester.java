package org.real.temp;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for MatrixTraversal using JUnit.
 */
public class Tester {
    

    @Test
    public void testEmptyMatrix() {
        // 异常值测试：空矩阵
        assertEquals("Should return an empty list for an empty matrix", 
                     new ArrayList<>(),
                     spiralTraversal(new int[0][]));
    }

    @Test
    public void testSingleElementMatrix() {
        // 基本逻辑功能测试：单元素矩阵
        int[][] matrix = {{42}};
        assertEquals("Should return the single element in the matrix", 
                     new ArrayList<>(List.of(42)), 
                     spiralTraversal(matrix));
    }

    @Test
    public void testSingleRowMatrix() {
        // 边界值测试：单行矩阵
        int[][] matrix = {{1, 2, 3, 4, 5}};
        assertEquals("Should return all elements in a single row", 
                     new ArrayList<>(List.of(1, 2, 3, 4, 5)),
                     spiralTraversal(matrix));
    }

    @Test
    public void testSingleColumnMatrix() {
        // 边界值测试：单列矩阵
        int[][] matrix = {{1}, {2}, {3}, {4}, {5}};
        assertEquals("Should return all elements in a single column", 
                     new ArrayList<>(List.of(1, 2, 3, 4, 5)), 
                     spiralTraversal(matrix));
    }

    @Test
    public void testGeneralCase() {
        // 基本逻辑功能测试：多行多列矩阵
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        assertEquals("Should return elements in spiral order for a general case matrix", 
                     new ArrayList<>(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5)), 
                     spiralTraversal(matrix));
    }
}