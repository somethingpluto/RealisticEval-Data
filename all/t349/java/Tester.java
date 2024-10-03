package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Tester {
    @Test
    public void testEmptyInput() {
        Answer<String> generator = new Answer<>();
        List<List<String>> input = new ArrayList<>();
        List<List<String>> expected = new ArrayList<>();
        assertEquals(expected, generator.generateCombinations(input), "Testing with empty input");
    }

    @Test
    public void testSingleEmptyList() {
        Answer<String> generator = new Answer<>();
        List<List<String>> input = Arrays.asList(new ArrayList<>());
        List<List<String>> expected = new ArrayList<>();
        assertEquals(expected, generator.generateCombinations(input), "Testing with a single empty list");
    }

    @Test
    public void testSingleNonEmptyList() {
        Answer<String> generator = new Answer<>();
        List<List<String>> input = Arrays.asList(Arrays.asList("a", "b", "c"));
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("a"), Arrays.asList("b"), Arrays.asList("c")
        );
        assertEquals(expected, generator.generateCombinations(input), "Testing with a single non-empty list");
    }

    @Test
    public void testMultipleLists() {
        Answer<String> generator = new Answer<>();
        List<List<String>> input = Arrays.asList(
                Arrays.asList("a", "b"),
                Arrays.asList("1", "2")
        );
        List<List<String>> expected = Arrays.asList(
                Arrays.asList("a", "1"), Arrays.asList("a", "2"),
                Arrays.asList("b", "1"), Arrays.asList("b", "2")
        );
        assertEquals(expected, generator.generateCombinations(input), "Testing with multiple lists");
    }

    @Test
    public void testInputContainingEmptyList() {
        Answer<String> generator = new Answer<>();
        List<List<String>> input = Arrays.asList(
                Arrays.asList("a", "b"),
                new ArrayList<>(),
                Arrays.asList("1", "2")
        );
        List<List<String>> expected = new ArrayList<>();
        assertEquals(expected, generator.generateCombinations(input), "Testing with an input that contains an empty list");
    }
}
