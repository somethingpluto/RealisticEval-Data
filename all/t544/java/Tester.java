package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testRemovesAllEvenNumbers() {
        int[] inputArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList(1, 3, 5, 7, 9);
        assertEquals(expected, result);
    }

    @Test
    public void testReturnsEmptyArrayWhenInputIsEmpty() {
        int[] inputArray = {};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList();
        assertEquals(expected, result);
    }

    @Test
    public void testReturnsSameArrayIfAllNumbersAreOdd() {
        int[] inputArray = {1, 3, 5, 7, 9};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList(1, 3, 5, 7, 9);
        assertEquals(expected, result);
    }

    @Test
    public void testReturnsEmptyArrayIfAllNumbersAreEven() {
        int[] inputArray = {2, 4, 6, 8, 10};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList();
        assertEquals(expected, result);
    }

    @Test
    public void testHandlesMixedPositiveAndNegativeNumbers() {
        int[] inputArray = {-3, -2, -1, 0, 1, 2, 3};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList(-3, -1, 1, 3);
        assertEquals(expected, result);
    }

    @Test
    public void testHandlesLargeNumbersAndZeroCorrectly() {
        int[] inputArray = {0, 1000000000, 1000000001, 1000000002, 1000000003};
        List<Integer> result = filterOutEvenNumbers(inputArray);
        List<Integer> expected = Arrays.asList(1000000001, 1000000003);
        assertEquals(expected, result);
    }
}