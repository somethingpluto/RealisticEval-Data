package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    // Test case 1: Basic unsorted array
    @Test
    public void testBasicUnsortedArray() {
        double[] arr = {12.4, 11.2, 13.5, 5.6, 6.7};
        double[] expected = {5.6, 6.7, 11.2, 12.4, 13.5};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 2: Already sorted array
    @Test
    public void testAlreadySortedArray() {
        double[] arr = {1.1, 2.2, 3.3, 4.4, 5.5};
        double[] expected = {1.1, 2.2, 3.3, 4.4, 5.5};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 3: Reverse sorted array
    @Test
    public void testReverseSortedArray() {
        double[] arr = {5.5, 4.4, 3.3, 2.2, 1.1};
        double[] expected = {1.1, 2.2, 3.3, 4.4, 5.5};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 4: Empty array
    @Test
    public void testEmptyArray() {
        double[] arr = {};
        double[] expected = {};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 5: Single element array
    @Test
    public void testSingleElementArray() {
        double[] arr = {3.3};
        double[] expected = {3.3};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 6: Array with duplicate values
    @Test
    public void testArrayWithDuplicates() {
        double[] arr = {2.2, 3.3, 2.2, 1.1, 3.3};
        double[] expected = {1.1, 2.2, 2.2, 3.3, 3.3};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }

    // Test case 7: Large numbers
    @Test
    public void testLargeNumbers() {
        double[] arr = {1e10, 1e9, 1e11, 1e8};
        double[] expected = {1e8, 1e9, 1e10, 1e11};
        Answer.insertionSort(arr);
        assertArrayEquals(expected, arr);
    }
}
