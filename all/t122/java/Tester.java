package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

import java.util.Arrays;
import java.util.List;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testReplacesRemovedElementsWithNewElement() {
        List<Object> inputArray = Arrays.asList("a", "b", "c", "d", "e");
        List<Object> expected = Arrays.asList("a", "z", "e");
        assertArrayEquals(expected.toArray(), safeSplice(inputArray, 3, 1, "z").toArray());
    }

    @Test
    public void testShouldRemoveSpecifiedElementsAndReplaceWithNewElement() {
        List<Object> inputArray = Arrays.asList(1, 2, 3, 4, 5);
        List<Object> expected = Arrays.asList(1, 99, 4, 5);
        assertArrayEquals(expected.toArray(), safeSplice(inputArray, 2, 1, 99).toArray());
    }

    @Test
    public void testShouldHandleRemovingElementsFromEnd() {
        List<Object> inputArray = Arrays.asList(1, 2, 3, 4, 5);
        List<Object> expected = Arrays.asList(1, 2, 3);
        assertArrayEquals(expected.toArray(), safeSplice(inputArray, 2, 3, null).toArray());
    }

    @Test
    public void testShouldHandleNoElementsRemoved() {
        List<Object> inputArray = Arrays.asList(1, 2, 3, 4, 5);
        List<Object> expected = Arrays.asList(1, 2, 99, 3, 4, 5);
        assertArrayEquals(expected.toArray(), safeSplice(inputArray, 0, 2, 99).toArray());
    }

    @Test
    public void testShouldHandleEmptyInputArray() {
        List<Object> inputArray = Arrays.asList();
        List<Object> expected = Arrays.asList(99);
        assertArrayEquals(expected.toArray(), safeSplice(inputArray, 1, 0, 99).toArray());
    }
}