package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.Before;
import org.junit.Test;

public class Tester {

    private BresenhamLine bresenhamLine;

    @Before
    public void setUp() {
        bresenhamLine = new BresenhamLine();
    }

    @Test
    public void testBresenhamLine() {
        // Test case 1: Vertical line
        List<Tuple<Integer, Integer>> result1 = bresenhamLine.bresenhamLine(0, 0, 0, 3);
        assertEquals(4, result1.size());
        assertTrue(result1.contains(new Tuple<>(0, 0)));
        assertTrue(result1.contains(new Tuple<>(0, 1)));
        assertTrue(result1.contains(new Tuple<>(0, 2)));
        assertTrue(result1.contains(new Tuple<>(0, 3)));

        // Test case 2: Horizontal line
        List<Tuple<Integer, Integer>> result2 = bresenhamLine.bresenhamLine(0, 0, 3, 0);
        assertEquals(4, result2.size());
        assertTrue(result2.contains(new Tuple<>(0, 0)));
        assertTrue(result2.contains(new Tuple<>(1, 0)));
        assertTrue(result2.contains(new Tuple<>(2, 0)));
        assertTrue(result2.contains(new Tuple<>(3, 0)));

        // Test case 3: Diagonal line
        List<Tuple<Integer, Integer>> result3 = bresenhamLine.bresenhamLine(0, 0, 3, 3);
        assertEquals(4, result3.size());
        assertTrue(result3.contains(new Tuple<>(0, 0)));
        assertTrue(result3.contains(new Tuple<>(1, 1)));
        assertTrue(result3.contains(new Tuple<>(2, 2)));
        assertTrue(result3.contains(new Tuple<>(3, 3)));

        // Test case 4: Line with negative slope
        List<Tuple<Integer, Integer>> result4 = bresenhamLine.bresenhamLine(0, 3, 3, 0);
        assertEquals(4, result4.size());
        assertTrue(result4.contains(new Tuple<>(0, 3)));
        assertTrue(result4.contains(new Tuple<>(1, 2)));
        assertTrue(result4.contains(new Tuple<>(2, 1)));
        assertTrue(result4.contains(new Tuple<>(3, 0)));
    }
}