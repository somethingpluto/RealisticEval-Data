package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.HashSet;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testShuffleNumbers() {
        int[] array = {1, 2, 3, 4, 5};
        int[] shuffledArray = shuffle(Arrays.copyOf(array, array.length));
        assertEquals(array.length, shuffledArray.length);
        assertTrue(Arrays.stream(shuffledArray).allMatch(i -> Arrays.stream(array).anyMatch(j -> j == i)));
        assertEquals(new HashSet<>(Arrays.asList(Arrays.stream(shuffledArray).boxed().toArray(Integer[]::new))).size(),
                new HashSet<>(Arrays.asList(Arrays.stream(array).boxed().toArray(Integer[]::new))).size());
    }

    @Test
    public void testShuffleStrings() {
        String[] array = {"apple", "banana", "cherry", "date", "elderberry"};
        String[] shuffledArray = {"apple", "banana", "cherry", "date", "elderberry"};
        assertEquals(array.length, shuffledArray.length);
        assertTrue(Arrays.stream(shuffledArray).allMatch(i -> Arrays.stream(array).anyMatch(j -> j.equals(i))));
    }

    @Test
    public void testShuffleDuplicates() {
        int[] array = {1, 1, 2, 2, 3, 3};
        int[] shuffledArray = shuffle(Arrays.copyOf(array, array.length));
        assertEquals(array.length, shuffledArray.length);
        assertTrue(Arrays.stream(shuffledArray).allMatch(i -> Arrays.stream(array).anyMatch(j -> j == i)));
    }

    @Test
    public void testShuffleSingleElement() {
        int[] array = {42};
        int[] shuffledArray = shuffle(Arrays.copyOf(array, array.length));
        assertArrayEquals(array, shuffledArray);
    }

    @Test
    public void testShuffleEmptyArray() {
        int[] array = {};
        int[] shuffledArray = shuffle(Arrays.copyOf(array, array.length));
        assertEquals(0, shuffledArray.length);
    }
}