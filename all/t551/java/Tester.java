package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Test with a standard range of edges.
     */
    @Test
    public void testBasicCase() {
        double[] edges = {1, 2, 3, 4};
        double[] expectedMids = {1.5, 2.5, 3.5};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }

    /**
     * Test with two edges (single interval).
     */
    @Test
    public void testSingleInterval() {
        double[] edges = {5, 10};
        double[] expectedMids = {7.5};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }

    /**
     * Test with multiple intervals.
     */
    @Test
    public void testMultipleIntervals() {
        double[] edges = {0, 1, 2, 3, 4, 5};
        double[] expectedMids = {0.5, 1.5, 2.5, 3.5, 4.5};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }

    /**
     * Test with negative edges.
     */
    @Test
    public void testNegativeEdges() {
        double[] edges = {-5, -3, -1, 1};
        double[] expectedMids = {-4.0, -2.0, 0.0};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }

    /**
     * Test with edges including zero.
     */
    @Test
    public void testZeroEdges() {
        double[] edges = {0, 1, 2};
        double[] expectedMids = {0.5, 1.5};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }

    /**
     * Test with floating-point edges.
     */
    @Test
    public void testFloatEdges() {
        double[] edges = {0.0, 1.5, 3.0};
        double[] expectedMids = {0.75, 2.25};
        assertArrayEquals(expectedMids, getMidsFromEdges(edges), 0.001);
    }
}