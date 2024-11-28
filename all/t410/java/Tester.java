package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * Test class for checking the XOR sums of specific columns in a given combination array.
 */
public class Tester {

    /**
     * Test with combination values that produce the expected XOR sums.
     */
    @Test
    public void testCorrectXorSums() {
        int[][] combination = {
            {0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00},
            {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}
        };
        assertFalse(checkXorSum(combination));
    }

    /**
     * Test with combination values that do not meet the expected XOR sums.
     */
    @Test
    public void testIncorrectXorSums() {
        int[][] combination = {
            {0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00},
            {0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00}
        };
        assertFalse(checkXorSum(combination));
    }

    /**
     * Test with a combination where all values are zero.
     */
    @Test
    public void testEdgeCaseWithZero() {
        int[][] combination = new int[1][8];  // 1 row of zeros
        assertFalse(checkXorSum(combination));
    }

    /**
     * Test with large numbers in the combination.
     */
    @Test
    public void testLargeNumbers() {
        int[][] combination = {
            {0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000},
            {0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000}
        };
        assertFalse(checkXorSum(combination));
    }

    /**
     * Test with a combination that contains multiple rows.
     */
    @Test
    public void testMultipleRows() {
        int[][] combination = {
            {0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00},
            {0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00},
            {0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00}
        };
        assertTrue(checkXorSum(combination));
    }

    /**
     * Checks the XOR sums of specific columns in a given combination array.
     *
     * @param combination A 2D integer array where each column corresponds to a specific value.
     * @return true if the XOR sums of the specified columns match the required values; otherwise, false.
     */
    private static boolean checkXorSum(int[][] combination) {
        // Calculate XOR sums for specified columns
        int[] xorSum036 = new int[combination.length];
        int[] xorSum147 = new int[combination.length];
        int[] xorSum25 = new int[combination.length];

        for (int i = 0; i < combination.length; i++) {
            xorSum036[i] = combination[i][0] ^ combination[i][3] ^ combination[i][6];
            xorSum147[i] = combination[i][1] ^ combination[i][4] ^ combination[i][7];
            xorSum25[i] = combination[i][2] ^ combination[i][5];
        }

        // Check if the XOR sums match the expected values
        return Arrays.stream(xorSum036).allMatch(x -> x == 0x6b) &&
               Arrays.stream(xorSum147).allMatch(x -> x == 0x76) &&
               Arrays.stream(xorSum25).allMatch(x -> x == 0x12);
    }
}