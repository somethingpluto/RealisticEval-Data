package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Test cases for the Floyd-Warshall shortest paths algorithm.
 */
public class Tester {

    @Test
    public void testBasicFunctionality() {
        // Basic test case with a simple graph
        List<List<Double>> matrix = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, 3.0, Double.POSITIVE_INFINITY, 7.0)),
            new ArrayList<>(Arrays.asList(8.0, 0.0, 2.0, Double.POSITIVE_INFINITY)),
            new ArrayList<>(Arrays.asList(5.0, Double.POSITIVE_INFINITY, 0.0, 1.0)),
            new ArrayList<>(Arrays.asList(2.0, Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, 0.0))
        ));
        List<List<Double>> expected = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, 3.0, 5.0, 6.0)),
            new ArrayList<>(Arrays.asList(5.0, 0.0, 2.0, 3.0)),
            new ArrayList<>(Arrays.asList(3.0, 6.0, 0.0, 1.0)),
            new ArrayList<>(Arrays.asList(2.0, 5.0, 7.0, 0.0))
        ));
        List<List<Double>> result = floydWarshallShortestPaths(matrix);
        assertEquals(expected, result, "Basic functionality test failed");
    }

    @Test
    public void testSingleVertexGraph() {
        // Test case with a single vertex graph (1x1 matrix)
        List<List<Double>> matrix = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0))
        ));
        List<List<Double>> expected = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0))
        ));
        List<List<Double>> result = floydWarshallShortestPaths(matrix);
        assertEquals(expected, result, "Single vertex graph test failed");
    }

    @Test
    public void testTwoVerticesGraph() {
        // Test case with two vertices
        List<List<Double>> matrix = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, 1.0)),
            new ArrayList<>(Arrays.asList(1.0, 0.0))
        ));
        List<List<Double>> expected = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, 1.0)),
            new ArrayList<>(Arrays.asList(1.0, 0.0))
        ));
        List<List<Double>> result = floydWarshallShortestPaths(matrix);
        assertEquals(expected, result, "Two vertices graph test failed");
    }

    @Test
    public void testLargeInfiniteWeights() {
        // Test case with infinite weights
        List<List<Double>> matrix = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, Double.POSITIVE_INFINITY)),
            new ArrayList<>(Arrays.asList(Double.POSITIVE_INFINITY, 0.0))
        ));
        List<List<Double>> expected = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, Double.POSITIVE_INFINITY)),
            new ArrayList<>(Arrays.asList(Double.POSITIVE_INFINITY, 0.0))
        ));
        List<List<Double>> result = floydWarshallShortestPaths(matrix);
        assertEquals(expected, result, "Large infinite weights test failed");
    }

    @Test
    public void testNegativeCycle() {
        // Test case with a negative cycle
        List<List<Double>> matrix = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(0.0, 1.0, Double.POSITIVE_INFINITY)),
            new ArrayList<>(Arrays.asList(Double.POSITIVE_INFINITY, 0.0, -1.0)),
            new ArrayList<>(Arrays.asList(-1.0, Double.POSITIVE_INFINITY, 0.0))
        ));
        List<List<Double>> expected = new ArrayList<>(Arrays.asList(
            new ArrayList<>(Arrays.asList(-1.0, 0.0, -1.0)),
            new ArrayList<>(Arrays.asList(-2.0, -1.0, -2.0)),
            new ArrayList<>(Arrays.asList(-2.0, -1.0, -2.0))
        ));
        List<List<Double>> result = floydWarshallShortestPaths(matrix);
        assertEquals(expected, result, "Negative cycle test failed");
    }
}
