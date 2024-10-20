package org.real.temp;

import org.junit.Test; // JUnit 4 Test annotation
import static org.junit.Assert.assertEquals; // JUnit 4 assertEquals
import java.util.Arrays;
import java.util.List;


import org.real.temp.*;
public class Tester {
    @Test
    public void testNonDecreasingSequence() {
        int[] nums = {5, 7, 4, 8, 6, 10, 2, 11};
        List<Integer> expected = Arrays.asList(5, 7, 8, 10, 11);
        assertEquals(expected, Answer.findLongestNonDecreasingSubsequence(nums));
    }

    @Test
    public void testAllIncreasing() {
        int[] nums = {1, 2, 3, 4, 5};
        List<Integer> expected = Arrays.asList(1, 2, 3, 4, 5);
        assertEquals(expected, Answer.findLongestNonDecreasingSubsequence(nums));
    }

    @Test
    public void testAllDecreasing() {
        int[] nums = {5, 4, 3, 2, 1};
        List<Integer> expected = Arrays.asList(5);
        assertEquals(expected, Answer.findLongestNonDecreasingSubsequence(nums));
    }

    @Test
    public void testSingleElement() {
        int[] nums = {10};
        List<Integer> expected = Arrays.asList(10);
        assertEquals(expected, Answer.findLongestNonDecreasingSubsequence(nums));
    }

    @Test
    public void testEmptyArray() {
        int[] nums = {};
        List<Integer> expected = Arrays.asList();
        assertEquals(expected, Answer.findLongestNonDecreasingSubsequence(nums));
    }
}
