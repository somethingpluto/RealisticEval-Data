package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testGenerateUniquePairsWithThreeElements() {
        String[] items = {"A", "B", "C"};
        List<List<String>> result = generateUniquePairs(items);
        List<List<String>> expected = Arrays.asList(
            Arrays.asList("A", "B"),
            Arrays.asList("A", "C"),
            Arrays.asList("B", "C")
        );
        assertEquals(expected, result);
    }

    @Test
    public void testGenerateUniquePairsWithTwoElements() {
        String[] items = {"A", "B"};
        List<List<String>> result = generateUniquePairs(items);
        List<List<String>> expected = Arrays.asList(
            Arrays.asList("A", "B")
        );
        assertEquals(expected, result);
    }

    @Test
    public void testGenerateUniquePairsWithEmptyArray() {
        String[] items = {};
        List<List<String>> result = generateUniquePairs(items);
        List<List<String>> expected = Arrays.asList();
        assertEquals(expected, result);
    }

    @Test
    public void testGenerateUniquePairsWithOneElement() {
        String[] items = {"A"};
        List<List<String>> result = generateUniquePairs(items);
        List<List<String>> expected = Arrays.asList();
        assertEquals(expected, result);
    }

    @Test
    public void testGenerateUniquePairsWithDifferentTypes() {
        Object[] items = {1, "A", new Object() { public String key = "value"; }};
        List<List<Object>> result = generateUniquePairs(items);
        List<List<Object>> expected = Arrays.asList(
            Arrays.asList(1, "A"),
            Arrays.asList(1, new Object() { public String key = "value"; }),
            Arrays.asList("A", new Object() { public String key = "value"; })
        );
        assertEquals(expected, result);
    }

    @Test
    public void testGenerateUniquePairsWithMoreThanThreeElements() {
        String[] items = {"A", "B", "C", "D"};
        List<List<String>> result = generateUniquePairs(items);
        List<List<String>> expected = Arrays.asList(
            Arrays.asList("A", "B"),
            Arrays.asList("A", "C"),
            Arrays.asList("A", "D"),
            Arrays.asList("B", "C"),
            Arrays.asList("B", "D"),
            Arrays.asList("C", "D")
        );
        assertEquals(expected, result);
    }
}