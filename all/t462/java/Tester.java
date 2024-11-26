package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSpiralOrder() {

        // Test case 1
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        List<Integer> expected1 = Arrays.asList(1, 2, 3, 6, 9, 8, 7, 4, 5);
        assertEquals(expected1, spiralOrder(matrix1));
    }

    @Test
    public void testcase2(){

        // Test case 2
        int[][] matrix2 = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12}
        };
        List<Integer> expected2 = Arrays.asList(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7);
        assertEquals(expected2, spiralOrder(matrix2));
    }

    @Test
    public void testcase3(){
        // Test case 3
        int[][] matrix3 = {};
        List<Integer> expected3 = Arrays.asList();
        assertEquals(expected3, spiralOrder(matrix3));
    }

    @Test
    public void testcase4(){
        // Test case 4
        int[][] matrix4 = {{1}};
        List<Integer> expected4 = Arrays.asList(1);
        assertEquals(expected4, spiralOrder(matrix4));
    }

    @Test
    public void testcase5(){
        // Test case 5
        int[][] matrix5 = {
                {1, 2},
                {3, 4},
                {5, 6}
        };
        List<Integer> expected5 = Arrays.asList(1, 2, 4, 6, 5, 3);
        assertEquals(expected5, spiralOrder(matrix5));
    }
}


