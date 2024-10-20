package org.real.temp;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static junit.framework.TestCase.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testBasicRotation() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(2, 3, 4, 1));
        assertEquals("Should rotate the list elements correctly", expectedList, rotateListElements(originalList));
    }

    @Test
    public void testSingleElementList() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(10));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(10));
        assertEquals("Single element list should remain unchanged", expectedList, rotateListElements(originalList));
    }

    @Test
    public void testEmptyList() {
        List<Integer> originalList = new ArrayList<>();
        List<Integer> expectedList = new ArrayList<>();
        assertEquals("Empty list should remain unchanged", expectedList, rotateListElements(originalList));
    }

    @Test
    public void testTwoElementList() {
        List<Integer> originalList = new ArrayList<>(Arrays.asList(5, 9));
        List<Integer> expectedList = new ArrayList<>(Arrays.asList(9, 5));
        assertEquals("Should correctly rotate a two-element list", expectedList, rotateListElements(originalList));
    }

    @Test
    public void testLargeList() {
        List<Integer> largeList = new ArrayList<>();
        for (int i = 1; i <= 1000; i++) {
            largeList.add(i);
        }
        List<Integer> expectedList = new ArrayList<>(largeList.subList(1, largeList.size()));
        expectedList.add(largeList.get(0));
        assertEquals("Should correctly rotate a large list", expectedList, rotateListElements(largeList));
    }
}