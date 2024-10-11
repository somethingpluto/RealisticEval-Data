package org.real.temp;

import java.util.Arrays;
import java.util.List;

public class Answer {
    
    /**
     * Given an integer array nums and find the length of the longest strictly increasing subsequence in it.
     * For example:
     *     input: [10, 9, 2, 5, 3, 7, 101, 18]
     *     output: 4
     *
     * @param nums The integer array.
     * @return The length of the longest strictly increasing subsequence.
     */
    public static int lengthOfLIS(List<Integer> nums) {
        if (nums == null || nums.isEmpty()) {
            return 0;
        }
        
        int n = nums.size();
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums.get(i) > nums.get(j)) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        
        int maxLength = 0;
        for (int length : dp) {
            maxLength = Math.max(maxLength, length);
        }
        
        return maxLength;
    }

    // Example usage
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(10, 9, 2, 5, 3, 7, 101, 18);
        System.out.println(lengthOfLIS(nums)); // Output: 4
    }
}