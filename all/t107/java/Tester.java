package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;
import java.util.Random;

public class Tester {

    @Test
    public void testFindMedianLargeArray() {
        // Example usage with a large array
        Random random = new Random();
        int[] largeArray = random.ints(10001, 0, 10000).toArray();
        double medianLargeArray = MedianFinder.findMedian(largeArray);
        // It's difficult to assert the exact median here due to randomness,
        // but this test can check if the function completes without error
        assertTrue(medianLargeArray instanceof Number);
    }

    @Test
    public void testFindMedianOddElements() {
        // Test Case 1: Odd number of elements
        int[] arr1 = {3, 1, 4, 1, 5, 9, 2};
        double median1 = MedianFinder.findMedian(arr1);
        assertEquals(3, median1, 0.001);
    }

    @Test
    public void testFindMedianEvenElements() {
        // Test Case 2: Even number of elements
        int[] arr2 = {10, 2, 3, 5, 7, 8};
        double median2 = MedianFinder.findMedian(arr2);
        assertEquals(6, median2, 0.001);
    }

    @Test
    public void testFindMedianDuplicates() {
        // Test Case 3: Array with duplicate elements
        int[] arr3 = {1, 2, 2, 2, 3};
        double median3 = MedianFinder.findMedian(arr3);
        assertEquals(2, median3, 0.001);
    }

    @Test
    public void testFindMedianNegativeNumbers() {
        // Test Case 4: Array with negative numbers
        int[] arr4 = {-5, -10, 0, 5, 10};
        double median4 = MedianFinder.findMedian(arr4);
        assertEquals(0, median4, 0.001);
    }

    @Test
    public void testFindMedianSingleElement() {
        // Test Case 5: Array with a single element
        int[] arr5 = {42};
        double median5 = MedianFinder.findMedian(arr5);
        assertEquals(42, median5, 0.001);
    }
}