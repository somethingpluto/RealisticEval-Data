package org.real.temp;

import org.junit.Test;
import org.junit.Assert;

import java.util.*;

public class Tester {

    @Test
    public void testGeneratesCombinationsForSingleKeyWithMultipleValues() {
        Map<String, List<Integer>> map = new HashMap<>();
        map.put("a", Arrays.asList(1, 2, 3));
        List<List<Integer>> expected = Arrays.asList(Arrays.asList(1), Arrays.asList(2), Arrays.asList(3));
        Assert.assertEquals(expected, generateCombinations(map));
    }

    @Test
    public void testGeneratesCombinationsForMultipleKeysWithSingleValues() {
        Map<String, List<Integer>> map = new HashMap<>();
        map.put("a", Collections.singletonList(1));
        map.put("b", Collections.singletonList(2));
        List<List<Integer>> expected = Collections.singletonList(Arrays.asList(1, 2));
        Assert.assertEquals(expected, generateCombinations(map));
    }

    @Test
    public void testGeneratesCombinationsForMultipleKeysWithMultipleValues() {
        Map<String, List<Integer>> map = new HashMap<>();
        map.put("a", Arrays.asList(1, 2));
        map.put("b", Arrays.asList(3, 4));
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(1, 3), Arrays.asList(1, 4),
                Arrays.asList(2, 3), Arrays.asList(2, 4)
        );
        Assert.assertEquals(expected, generateCombinations(map));
    }

    @Test
    public void testHandlesEmptyMap() {
        Map<String, List<Integer>> map = new HashMap<>();
        List<List<Integer>> expected = Collections.singletonList(Collections.emptyList());
        Assert.assertEquals(expected, generateCombinations(map));
    }

    @Test
    public void testHandlesKeysWithEmptyArraysAsValues() {
        Map<String, List<Integer>> map = new HashMap<>();
        map.put("a", Collections.emptyList());
        map.put("b", Arrays.asList(1, 2));
        List<List<Integer>> expected = Collections.emptyList();
        Assert.assertEquals(expected, generateCombinations(map));
    }

    // Assuming generateCombinations method is implemented in this class or imported
    public List<List<Integer>> generateCombinations(Map<String, List<Integer>> map) {
        // Implementation goes here
        return new ArrayList<>(); // Placeholder
    }
}