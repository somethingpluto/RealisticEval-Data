package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.*;

public class Tester {

    private Map<String, List<Pair<String, Integer>>> graph1;
    private Map<String, List<Pair<String, Integer>>> graph2;
    private Map<String, List<Pair<String, Integer>>> graphWithIsolatedNode;
    private Map<String, List<Pair<String, Integer>>> graphWithNegativeWeight;

    @Before
    public void setUp() {
        // Sample graphs for testing
        graph1 = new HashMap<>();
        graph1.put("A", Arrays.asList(new Pair<>("B", 1), new Pair<>("C", 4)));
        graph1.put("B", Arrays.asList(new Pair<>("A", 1), new Pair<>("C", 2), new Pair<>("D", 5)));
        graph1.put("C", Arrays.asList(new Pair<>("A", 4), new Pair<>("B", 2), new Pair<>("D", 1)));
        graph1.put("D", Arrays.asList(new Pair<>("B", 5), new Pair<>("C", 1)));

        graph2 = new HashMap<>();
        graph2.put("A", Arrays.asList(new Pair<>("B", 2)));
        graph2.put("B", Arrays.asList(new Pair<>("A", 2), new Pair<>("C", 3)));
        graph2.put("C", Arrays.asList(new Pair<>("B", 3), new Pair<>("D", 1)));
        graph2.put("D", Arrays.asList(new Pair<>("C", 1)));

        graphWithIsolatedNode = new HashMap<>();
        graphWithIsolatedNode.put("A", Arrays.asList(new Pair<>("B", 1)));
        graphWithIsolatedNode.put("B", Arrays.asList(new Pair<>("A", 1)));
        graphWithIsolatedNode.put("C", new ArrayList<>());  // Isolated node

        graphWithNegativeWeight = new HashMap<>();
        graphWithNegativeWeight.put("A", Arrays.asList(new Pair<>("B", 2), new Pair<>("C", 1)));
        graphWithNegativeWeight.put("B", Arrays.asList(new Pair<>("D", 3)));
        graphWithNegativeWeight.put("C", Arrays.asList(new Pair<>("B", -1), new Pair<>("D", 4)));
        graphWithNegativeWeight.put("D", new ArrayList<>());
    }

    @Test
    public void testShortestPathsGraph1() {
        // Test shortest paths in a normal graph.
        Map<String, Integer> expected = new HashMap<>();
        expected.put("A", 0);
        expected.put("B", 1);
        expected.put("C", 3);
        expected.put("D", 4);

        Map<String, Integer> result = dijkstra(graph1, "A");
        assertEquals(expected, result);
    }

    @Test
    public void testShortestPathsGraph2() {
        // Test shortest paths in a different normal graph.
        Map<String, Integer> expected = new HashMap<>();
        expected.put("A", 0);
        expected.put("B", 2);
        expected.put("C", 5);
        expected.put("D", 6);

        Map<String, Integer> result = dijkstra(graph2, "A");
        assertEquals(expected, result);
    }

    @Test
    public void testShortestPathsWithIsolatedNode() {
        // Test shortest paths with an isolated node.
        Map<String, Integer> expected = new HashMap<>();
        expected.put("A", 0);
        expected.put("B", 1);
        expected.put("C", Integer.MAX_VALUE);

        Map<String, Integer> result = dijkstra(graphWithIsolatedNode, "A");
        assertEquals(expected, result);
    }

    @Test
    public void testStartingAtIsolatedNode() {
        // Test when starting at an isolated node.
        Map<String, Integer> expected = new HashMap<>();
        expected.put("C", 0);
        expected.put("A", Integer.MAX_VALUE);
        expected.put("B", Integer.MAX_VALUE);

        Map<String, Integer> result = dijkstra(graphWithIsolatedNode, "C");
        assertEquals(expected, result);
    }
}