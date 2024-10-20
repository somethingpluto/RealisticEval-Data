package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testEmptyArray() {
        int[] emptyArray = {};
        mergeSort(emptyArray, 0, emptyArray.length - 1);
        assertArrayEquals(new int[]{}, emptyArray);
    }

    @Test
    public void testSingleElementArray() {
        int[] singleElement = {1};
        mergeSort(singleElement, 0, singleElement.length - 1);
        assertArrayEquals(new int[]{1}, singleElement);
    }

    @Test
    public void testSortedArray() {
        int[] sortedArray = {1, 2, 3, 4, 5};
        mergeSort(sortedArray, 0, sortedArray.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, sortedArray);
    }

    @Test
    public void testReverseSortedArray() {
        int[] reverseSortedArray = {5, 4, 3, 2, 1};
        mergeSort(reverseSortedArray, 0, reverseSortedArray.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, reverseSortedArray);
    }

    @Test
    public void testRandomArray() {
        int[] randomArray = {38, 27, 43, 3, 9, 82, 10};
        int[] expectedSortedArray = {3, 9, 10, 27, 38, 43, 82};
        mergeSort(randomArray, 0, randomArray.length - 1);
        assertArrayEquals(expectedSortedArray, randomArray);
    }
}