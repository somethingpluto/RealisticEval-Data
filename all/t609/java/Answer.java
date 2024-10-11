package org.real.temp;

import java.util.HashMap;

public class Answer {

    /**
     * Finds two indices of numbers in the array that sum up to the target value.
     *
     * @param nums   the input array of integers
     * @param target the target sum value
     * @return an array containing the indices of the two numbers
     * @throws IllegalArgumentException if no such indices are found
     */
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store numbers and their corresponding indices
        HashMap<Integer, Integer> numsMap = new HashMap<>();

        // First loop to populate the HashMap
        for (int i = 0; i < nums.length; i++) {
            numsMap.put(nums[i], i);
        }

        // Second loop to find the two indices
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i]; // Calculate the complement
            // Check if the complement exists and is not the same index
            if (numsMap.containsKey(complement) && numsMap.get(complement) != i) {
                return new int[] { i, numsMap.get(complement) }; // Return the indices
            }
        }

        // If no solution is found, throw an exception
        throw new IllegalArgumentException("No two sum solution");
    }
}