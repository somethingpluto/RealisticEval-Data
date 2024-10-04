package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.*;
public class Tester{
    /**
     * Test when the target is present in the array.
     */
    @Test
    public void testTargetPresent() {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 7;
        int result = Answer.binarySearchClosest(array, target);
        assertEquals(3, result, "Target should be found at index 3.");
    }

    /**
     * Test when the target is not present and the closest element is smaller.
     */
    @Test
    public void testClosestElementSmaller() {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 6;
        int result = Answer.binarySearchClosest(array, target);
        assertEquals(2, result, "Closest element should be 5 at index 2.");
    }

    /**
     * Test when the target is not present and the closest element is larger.
     */
    @Test
    public void testClosestElementLarger() {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 8;
        int result = Answer.binarySearchClosest(array, target);
        assertEquals(3, result, "Closest element should be 7 at index 3.");
    }

    /**
     * Test when the target is smaller than all elements in the array.
     */
    @Test
    public void testTargetSmallerThanAll() {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 0;
        int result = Answer.binarySearchClosest(array, target);
        assertEquals(0, result, "Closest element should be 1 at index 0.");
    }

    /**
     * Test when the target is larger than all elements in the array.
     */
    @Test
    public void testTargetLargerThanAll() {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 12;
        int result = Answer.binarySearchClosest(array, target);
        assertEquals(5, result, "Closest element should be 11 at index 5.");
    }
}
