package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testEmptyLists() {
        Answer answer = new Answer();
        List<List<String>> inputLists = new ArrayList<>();
        List<List<String>> expected = new ArrayList<>();
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleEmptyList() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(new ArrayList<>());
        List<List<String>> expected = new ArrayList<>();
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleItemLists() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(
                Arrays.asList("A"),
                Arrays.asList("B"),
                Arrays.asList("C")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("A", "B", "C")
        );
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testMultipleItemsInSingleList() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(
                Arrays.asList("A", "B"),
                Arrays.asList("1", "2")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("A", "1"),
                Arrays.asList("A", "2"),
                Arrays.asList("B", "1"),
                Arrays.asList("B", "2")
        );
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testAllItemsDifferent() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(
                Arrays.asList("A", "B"),
                Arrays.asList("1", "2"),
                Arrays.asList("X", "Y")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("A", "1", "X"),
                Arrays.asList("A", "1", "Y"),
                Arrays.asList("A", "2", "X"),
                Arrays.asList("A", "2", "Y"),
                Arrays.asList("B", "1", "X"),
                Arrays.asList("B", "1", "Y"),
                Arrays.asList("B", "2", "X"),
                Arrays.asList("B", "2", "Y")
        );
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testDifferentSizes() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(
                Arrays.asList("A"),
                Arrays.asList("1", "2"),
                Arrays.asList("X", "Y", "Z")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("A", "1", "X"),
                Arrays.asList("A", "1", "Y"),
                Arrays.asList("A", "1", "Z"),
                Arrays.asList("A", "2", "X"),
                Arrays.asList("A", "2", "Y"),
                Arrays.asList("A", "2", "Z")
        );
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleItemInOneList() {
        Answer answer = new Answer();
        List<List<String>> inputLists = Arrays.asList(
                Arrays.asList("A"),
                Arrays.asList("B"),
                Arrays.asList("C", "D")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("A", "B", "C"),
                Arrays.asList("A", "B", "D")
        );
        List<List<String>> result = answer.generateCombinations(inputLists);
        assertEquals(expected, result);
    }
}
