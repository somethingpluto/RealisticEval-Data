package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.List;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testHorizontalLine() {
        List<int[]> expected = Arrays.asList(
                new int[]{1, 5},
                new int[]{2, 5},
                new int[]{3, 5},
                new int[]{4, 5},
                new int[]{5, 5}
        );
        List<int[]> actual = bresenhamLine(1, 5, 5, 5);
        // Check if the sizes of the lists are equal
        assertEquals(expected.size(), actual.size());

        // Compare each int array in the lists
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), actual.get(i));
        }
    }

    @Test
    public void testVerticalLine() {
        List<int[]> expected = Arrays.asList(
                new int[]{3, 2},
                new int[]{3, 3},
                new int[]{3, 4},
                new int[]{3, 5},
                new int[]{3, 6}
        );
        List<int[]> actual = bresenhamLine(3, 2, 3, 6);
        // Check if the sizes of the lists are equal
        assertEquals(expected.size(), actual.size());

        // Compare each int array in the lists
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), actual.get(i));
        }
    }

    @Test
    public void testDiagonalLine() {
        List<int[]> expected = Arrays.asList(
                new int[]{2, 2},
                new int[]{3, 3},
                new int[]{4, 4},
                new int[]{5, 5},
                new int[]{6, 6}
        );
        List<int[]> actual = bresenhamLine(2, 2, 6, 6);
        // Check if the sizes of the lists are equal
        assertEquals(expected.size(), actual.size());

        // Compare each int array in the lists
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), actual.get(i));
        }
    }

    @Test
    public void testSteepSlope() {
        List<int[]> expected = Arrays.asList(
                new int[]{1, 1},
                new int[]{2, 2},
                new int[]{2, 3},
                new int[]{3, 4},
                new int[]{3, 5},
                new int[]{4, 6}
        );
        List<int[]> actual = bresenhamLine(1, 1, 4, 6);
        // Check if the sizes of the lists are equal
        assertEquals(expected.size(), actual.size());

        // Compare each int array in the lists
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), actual.get(i));
        }
    }

    @Test
    public void testNegativeSlope() {
        List<int[]> expected = Arrays.asList(
                new int[]{5, 1},
                new int[]{4, 2},
                new int[]{3, 3},
                new int[]{2, 4},
                new int[]{1, 5}
        );
        List<int[]> actual = bresenhamLine(5, 1, 1, 5);
        // Check if the sizes of the lists are equal
        assertEquals(expected.size(), actual.size());

        // Compare each int array in the lists
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), actual.get(i));
        }
    }
}