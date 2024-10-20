package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.real.temp.Answer.*;

public class Tester {


    @Test
    public void testEvenDivision() {
        List<Integer> lst = Arrays.asList(1, 2, 3, 4, 5, 6);
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(1, 2),
                Arrays.asList(3, 4),
                Arrays.asList(5, 6)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testUnevenDivision() {
        List<Integer> lst = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5),
                Arrays.asList(6, 7)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testMorePartsThanItems() {
        List<Integer> lst = Arrays.asList(1, 2, 3);
        int n = 5;
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(1),
                Arrays.asList(2),
                Arrays.asList(3),
                Arrays.asList(),
                Arrays.asList()
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testSingleElement() {
        List<Integer> lst = Arrays.asList(1);
        int n = 1;
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(1)
        );
        assertEquals(expected, divideList(lst, n));
    }

    @Test
    public void testEmptyList() {
        List<Integer> lst = Arrays.asList();
        int n = 3;
        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(),
                Arrays.asList(),
                Arrays.asList()
        );
        assertEquals(expected, divideList(lst, n));
    }
}