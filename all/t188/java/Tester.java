package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.real.temp.Answer.*;
public class Tester {

    public static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }

    @Test
    public void testShellSortBasicFunctionality() {
        // Test Case 1: Already sorted array
        int[] arr1 = {1, 2, 3, 4, 5};
        Answer.shellSort(arr1);
        assertTrue(isSorted(arr1));

        // Test Case 2: Reverse sorted array
        int[] arr2 = {5, 4, 3, 2, 1};
        Answer.shellSort(arr2);
        assertTrue(isSorted(arr2));

        // Test Case 3: Array with duplicate elements
        int[] arr3 = {4, 2, 2, 4, 1};
        Answer.shellSort(arr3);
        assertTrue(isSorted(arr3));

        // Test Case 4: Array with negative numbers
        int[] arr4 = {-3, -1, -4, -2, 0};
        Answer.shellSort(arr4);
        assertTrue(isSorted(arr4));

        // Test Case 5: Empty array
        int[] arr5 = {};
        Answer.shellSort(arr5);
        assertTrue(isSorted(arr5));
    }
}