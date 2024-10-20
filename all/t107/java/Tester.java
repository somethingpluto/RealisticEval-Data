package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

import org.junit.Test;

public class Tester {


    @Test
    public void testFindMedianOddElements() {
        // Test Case 1: Odd number of elements
        int[] arr1 = {3, 1, 4, 1, 5, 9, 2};
        double median1 = findMedian(arr1);
        assertEquals(3, median1, 0.001);
    }

    @Test
    public void testFindMedianEvenElements() {
        // Test Case 2: Even number of elements
        int[] arr2 = {10, 2, 3, 5, 7, 8};
        double median2 = findMedian(arr2);
        assertEquals(6, median2, 0.001);
    }

    @Test
    public void testFindMedianDuplicates() {
        // Test Case 3: Array with duplicate elements
        int[] arr3 = {1, 2, 2, 2, 3};
        double median3 = findMedian(arr3);
        assertEquals(2, median3, 0.001);
    }

    @Test
    public void testFindMedianNegativeNumbers() {
        // Test Case 4: Array with negative numbers
        int[] arr4 = {-5, -10, 0, 5, 10};
        double median4 = findMedian(arr4);
        assertEquals(0, median4, 0.001);
    }

    @Test
    public void testFindMedianSingleElement() {
        // Test Case 5: Array with a single element
        int[] arr5 = {42};
        double median5 = findMedian(arr5);
        assertEquals(42, median5, 0.001);
    }
}