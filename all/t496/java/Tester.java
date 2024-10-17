package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.List;

/**
 * Test class for verifying the correctness of the Pascal's Triangle row generation.
 */
public class Tester {

    /**
     * Tests the 0th row of Pascal's Triangle.
     */
    @Test
    public void testRow0() {
        List<Long> expected = Arrays.asList(1L);
        assertEquals(expected, pascalTriangleRow(0));
    }

    /**
     * Tests the 1st row of Pascal's Triangle.
     */
    @Test
    public void testRow1() {
        List<Long> expected = Arrays.asList(1L, 1L);
        assertEquals(expected, pascalTriangleRow(1));
    }

    /**
     * Tests the 2nd row of Pascal's Triangle.
     */
    @Test
    public void testRow2() {
        List<Long> expected = Arrays.asList(1L, 2L, 1L);
        assertEquals(expected, pascalTriangleRow(2));
    }

    /**
     * Tests the 3rd row of Pascal's Triangle.
     */
    @Test
    public void testRow3() {
        List<Long> expected = Arrays.asList(1L, 3L, 3L, 1L);
        assertEquals(expected, pascalTriangleRow(3));
    }

    /**
     * Tests the 4th row of Pascal's Triangle.
     */
    @Test
    public void testRow4() {
        List<Long> expected = Arrays.asList(1L, 4L, 6L, 4L, 1L);
        assertEquals(expected, pascalTriangleRow(4));
    }

    /**
     * Tests the 5th row of Pascal's Triangle.
     */
    @Test
    public void testRow5() {
        List<Long> expected = Arrays.asList(1L, 5L, 10L, 10L, 5L, 1L);
        assertEquals(expected, pascalTriangleRow(5));
    }

    /**
     * Generates the ith row of Pascal's Triangle.
     *
     * @param i the row index (0-indexed)
     * @return a List representing the ith row of Pascal's Triangle
     */
    private List<Long> pascalTriangleRow(int i) {
        List<Long> row = new ArrayList<>();
        for (int k = 0; k <= i; k++) {
            row.add(combination(i, k));
        }
        return row;
    }

    /**
     * Calculates the combination (n choose k).
     *
     * @param n the total number of items
     * @param k the number of items to choose
     * @return the combination value
     */
    private static long combination(int n, int k) {
        long result = 1;
        if (k > n - k) {
            k = n - k;
        }
        for (int i = 0; i < k; ++i) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }
}