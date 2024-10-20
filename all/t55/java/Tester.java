package org.real.temp;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;


public class Tester {

    @Test
    public void testBasicArray() {
        // Test with a basic array where multiple removals are needed.
        assertEquals(3, minRemovalsToMakeUnique(List.of(3, 3, 1, 2, 2, 1)));
    }

    @Test
    public void testAllIdentical() {
        // Test an array where all elements are identical.
        assertEquals(3, minRemovalsToMakeUnique(List.of(4, 4, 4, 4)));
    }

    @Test
    public void testAllUnique() {
        // Test an array where all elements are already unique.
        assertEquals(0, minRemovalsToMakeUnique(List.of(1, 2, 3, 4)));
    }

    @Test
    public void testEmptyArray() {
        // Test an empty array.
        assertEquals(0, minRemovalsToMakeUnique(List.of()));
    }

    @Test
    public void testComplexCase() {
        // Test a more complex case with a larger array.
        assertEquals(6, minRemovalsToMakeUnique(List.of(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)));
    }
}