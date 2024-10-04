package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private final Answer answer = new Answer();

    @Test
    public void testValidPair() {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] expected = {0, 1}; // 2 + 7 = 9
        assertArrayEquals(expected, answer.twoSum(nums, target));
    }

    @Test
    public void testNegativeNumbers() {
        int[] nums = {-1, -2, -3, -4, -5};
        int target = -8;
        int[] expected = {2, 4}; // -3 + -5 = -8
        assertArrayEquals(expected, answer.twoSum(nums, target));
    }

    @Test
    public void testZeroSum() {
        int[] nums = {0, 4, 3, 0};
        int target = 0;
        int[] expected = {0, 3}; // 0 + 0 = 0
        assertArrayEquals(expected, answer.twoSum(nums, target));
    }

    @Test
    public void testNoSolution() {
        int[] nums = {1, 2, 3, 4, 5};
        int target = 10;
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            answer.twoSum(nums, target);
        });
        assertEquals("No two sum solution", exception.getMessage());
    }

    @Test
    public void testSameNumberTwice() {
        int[] nums = {3, 3};
        int target = 6;
        int[] expected = {0, 1}; // 3 + 3 = 6
        assertArrayEquals(expected, answer.twoSum(nums, target));
    }

    @Test
    public void testLargeNumbers() {
        int[] nums = {Integer.MAX_VALUE, Integer.MIN_VALUE, 0, 1};
        int target = 1;
        int[] expected = {2, 3}; // 0 + 1 = 1
        assertArrayEquals(expected, answer.twoSum(nums, target));
    }
}