package org.real.temp;

import java.util.List;

public class Answer {
    public static int lengthOfLIS(List<Integer> nums) {
        /**
         * Given an array of integers nums, find the length of the longest strictly increasing subsequence in it.
         *
         * @param nums List of integers
         * @return Length of the longest strictly increasing subsequence
         */
        if (nums == null || nums.isEmpty()) {
            return 0;
        }

        int n = nums.size();
        int[] dp = new int[n];
        int maxLength = 1;

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums.get(i) > nums.get(j)) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLength = Math.max(maxLength, dp[i]);
        }

        return maxLength;
    }
}