package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testLengthOfLIS() {
        // Test case 1
        int[] nums1 = {10, 9, 2, 5, 3, 7, 101, 18};
        assertEquals(4, lengthOfLIS(nums1), "Test case 1 failed");

        // Test case 2
        int[] nums2 = {0, 1, 0, 3, 2, 3};
        assertEquals(4, lengthOfLIS(nums2), "Test case 2 failed");

        // Test case 3
        int[] nums3 = {7, 7, 7, 7, 7, 7, 7};
        assertEquals(1, lengthOfLIS(nums3), "Test case 3 failed");

        // Test case 4
        int[] nums4 = {};
        assertEquals(0, lengthOfLIS(nums4), "Test case 4 failed");

        // Test case 5
        int[] nums5 = {1};
        assertEquals(1, lengthOfLIS(nums5), "Test case 5 failed");
    }

    private int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int n = nums.length;
        int[] dp = new int[n];
        int maxLength = 1;

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLength = Math.max(maxLength, dp[i]);
        }

        return maxLength;
    }
}