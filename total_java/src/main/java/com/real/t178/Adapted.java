package com.real.t178;
import java.util.ArrayList;
import java.util.List;
public class Adapted {
    public static List<Integer> findLongestNonDecreasingSubsequence(int[] nums) {
        if (nums == null || nums.length == 0) {
            return new ArrayList<>();
        }

        int n = nums.length;
        int[] dp = new int[n];
        int[] previous = new int[n];

        // Initialize dp and previous arrays
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            previous[i] = -1;
        }

        int maxLength = 1;
        int lastIndex = 0;

        // Calculate the length of the longest non-decreasing subsequence
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] >= nums[j] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    previous[i] = j;
                }
            }

            // Update maxLength and lastIndex
            if (dp[i] > maxLength) {
                maxLength = dp[i];
                lastIndex = i;
            }
        }

        // Reconstruct the longest non-decreasing subsequence
        List<Integer> subsequence = new ArrayList<>();
        while (lastIndex != -1) {
            subsequence.add(0, nums[lastIndex]);
            lastIndex = previous[lastIndex];
        }

        return subsequence;
    }
}
