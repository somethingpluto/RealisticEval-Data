package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testBinarySearch_TargetPresent() {
        int[] sortedArray = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int target = 5;
        int expectedIndex = 4; // Index of target 5
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }

    @Test
    public void testBinarySearch_TargetNotPresent() {
        int[] sortedArray = {1, 3, 5, 7, 9};
        int target = 4;
        int expectedIndex = -1; // Target not found
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }

    @Test
    public void testBinarySearch_TargetAtBeginning() {
        int[] sortedArray = {1, 2, 3, 4, 5};
        int target = 1;
        int expectedIndex = 0; // Index of target 1
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }

    @Test
    public void testBinarySearch_TargetAtEnd() {
        int[] sortedArray = {2, 4, 6, 8, 10};
        int target = 10;
        int expectedIndex = 4; // Index of target 10
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }

    @Test
    public void testBinarySearch_EmptyArray() {
        int[] sortedArray = {};
        int target = 1;
        int expectedIndex = -1; // Target not found in empty array
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }

    @Test
    public void testBinarySearch_NegativeNumbers() {
        int[] sortedArray = {-10, -5, 0, 5, 10};
        int target = -5;
        int expectedIndex = 1; // Index of target -5
        int resultIndex = Answer.binarySearch(sortedArray, target);
        assertEquals(expectedIndex, resultIndex);
    }
}