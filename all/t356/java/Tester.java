package org.real.temp;

import org.junit.Test;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testBubbleSort() {
        // Test Case 1: Sorting an already sorted array
        List<Integer> arr1 = Arrays.asList(1, 2, 3, 4, 5);
        Answer.bubbleSort(arr1);
        assertEquals(Arrays.asList(1, 2, 3, 4, 5), arr1);

        // Test Case 2: Sorting a reverse sorted array
        List<Integer> arr2 = Arrays.asList(5, 4, 3, 2, 1);
        Answer.bubbleSort(arr2);
        assertEquals(Arrays.asList(1, 2, 3, 4, 5), arr2);

        // Test Case 3: Sorting an array with duplicate elements
        List<Integer> arr3 = Arrays.asList(3, 1, 2, 3, 2);
        Answer.bubbleSort(arr3);
        assertEquals(Arrays.asList(1, 2, 2, 3, 3), arr3);

        // Test Case 4: Sorting an array with a single element
        List<Integer> arr4 = Arrays.asList(1);
        Answer.bubbleSort(arr4);
        assertEquals(Arrays.asList(1), arr4);

        // Test Case 5: Sorting an empty array
        List<Integer> arr5 = Arrays.asList();
        Answer.bubbleSort(arr5);
        assertEquals(Arrays.asList(), arr5);
    }
}