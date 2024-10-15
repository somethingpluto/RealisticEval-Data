package org.real.temp;

import org.junit.Test;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

import static org.junit.Assert.assertEquals;

public class Tester {

    // Qualification function that checks if a number is greater than 10
    private Predicate<Integer> isGreaterThanTen = num -> num > 10;

    @Test
    public void testFiltersOutNumbersLessThanOrEqualToTen() {
        List<Integer> unfilteredList = Arrays.asList(5, 12, 3, 18, 7, 10, 15);
        List<Integer> result = Answer.filterList(unfilteredList, isGreaterThanTen);
        assertEquals(Arrays.asList(12, 18, 15), result);
    }

    @Test
    public void testReturnsEmptyListWhenAllElementsAreDisqualified() {
        List<Integer> unfilteredList = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> result = Answer.filterList(unfilteredList, isGreaterThanTen);
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void testReturnsSameListWhenAllElementsAreQualified() {
        List<Integer> unfilteredList = Arrays.asList(11, 12, 15, 20);
        List<Integer> result = Answer.filterList(unfilteredList, isGreaterThanTen);
        assertEquals(Arrays.asList(11, 12, 15, 20), result);
    }

    @Test
    public void testHandlesEmptyListInput() {
        List<Integer> unfilteredList = Arrays.asList();
        List<Integer> result = Answer.filterList(unfilteredList, isGreaterThanTen);
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void testFiltersOutStringsBasedOnLength() {
        Predicate<String> isLongerThanThreeChars = str -> str.length() > 3;
        List<String> unfilteredList = Arrays.asList("a", "ab", "abc", "abcd", "abcde");
        List<String> result = Answer.filterList(unfilteredList, isLongerThanThreeChars);
        assertEquals(Arrays.asList("abcd", "abcde"), result);
    }

    @Test
    public void testCorrectlyFiltersArrayWithMixedTypes() {
        Predicate<Object> isString = item -> item instanceof String;
        List<Object> unfilteredList = Arrays.asList(1, "hello", true, "world", null);
        List<Object> result = Answer.filterList(unfilteredList, isString);
        assertEquals(Arrays.asList("hello", "world"), result);
    }

    @Test
    public void testFiltersBasedOnObjectProperty() {
        Predicate<Item> hasValueGreaterThanFive = obj -> obj.value > 5;
        List<Item> unfilteredList = Arrays.asList(new Item(3), new Item(5), new Item(7));
        List<Item> result = Answer.filterList(unfilteredList, hasValueGreaterThanFive);
        assertEquals(Arrays.asList(new Item(7)), result);
    }

    @Test
    public void testReturnsEmptyListWhenNoQualifyingFunctionProvided() {
        List<Integer> unfilteredList = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> result = Answer.filterList(unfilteredList, num -> false); // Always returns false
        assertEquals(Arrays.asList(), result);
    }

    // Helper class for the object property test
    private static class Item {
        int value;

        Item(int value) {
            this.value = value;
        }
    }
}