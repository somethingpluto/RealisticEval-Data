package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testIdenticalArraysSameOrder() {
        Integer[] arr1 = {1, 2, 3};
        Integer[] arr2 = {1, 2, 3};
        assertTrue(compareArrays(arr1, arr2));
    }

    @Test
    public void testIdenticalArraysDifferentOrder() {
        Integer[] arr1 = {3, 2, 1};
        Integer[] arr2 = {1, 2, 3};
        assertTrue(compareArrays(arr1, arr2));
    }

    @Test
    public void testDifferentElements() {
        Integer[] arr1 = {1, 2, 3};
        Integer[] arr2 = {4, 5, 6};
        assertFalse(compareArrays(arr1, arr2));
    }

    @Test
    public void testDifferentLengths() {
        Integer[] arr1 = {1, 2, 3};
        Integer[] arr2 = {1, 2};
        assertFalse(compareArrays(arr1, arr2));
    }

    @Test
    public void testDuplicateElementsSameUniqueSet() {
        Integer[] arr1 = {1, 1, 2, 3, 3};
        Integer[] arr2 = {3, 2, 1, 1};
        assertTrue(compareArrays(arr1, arr2));
    }

    // Assuming compareArrays method is defined elsewhere in the class or imported
    public static <T> boolean compareArrays(T[] arr1, T[] arr2) {
        // Implementation of compareArrays method
    }
}