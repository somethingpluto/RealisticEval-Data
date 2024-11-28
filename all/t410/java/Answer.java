package org.real.temp;

import java.util.Arrays;

public class Answer {
    public static void main(String[] args) {
        // Example usage
        int[][] combination = {
            {0, 1, 2, 3, 4, 5, 6, 7},
            {1, 0, 3, 2, 5, 4, 7, 6}
        };

        boolean result = checkXorSum(combination);
        System.out.println("Result: " + result);
    }

    /**
     * Checks the XOR sums of specific columns in a given combination array.
     *
     * @param combination A 2D integer array where each column corresponds to a specific value.
     * @return True if the XOR sums of the specified columns match the required values; otherwise, False.
     */
    public static boolean checkXorSum(int[][] combination) {
        // Ensure that combination is an array of integers
        // In Java, it is already an array of integers, so no conversion is needed

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