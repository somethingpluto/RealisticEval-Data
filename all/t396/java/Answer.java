package org.real.temp;

import java.util.ArrayList;
import java.util.Arrays;

public class Answer {

    /**
     * Given an array of integers nums, find the length of the longest strictly increasing subsequence.
     *
     * @param nums the array of integers
     * @return the length of the longest strictly increasing subsequence
     */
    public static int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
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

    public static void main(String[] args) {
        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("Length of the longest strictly increasing subsequence: " + lengthOfLIS(nums));
    }
}