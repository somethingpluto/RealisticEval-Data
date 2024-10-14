package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class Tester {

    private TopologicalSort topologicalSort;

    @Before
    public void setUp() {
        topologicalSort = new TopologicalSort();
    }

    @Test
    public void testTopologicalSortDfs() {
        List<Integer> vertices = new ArrayList<>();
        vertices.add(1);
        vertices.add(2);
        vertices.add(3);
        vertices.add(4);

        List<List<Integer>> edges = new ArrayList<>();
        edges.add(List.of(1, 2));
        edges.add(List.of(1, 3));
        edges.add(List.of(2, 4));
        edges.add(List.of(3, 4));

        List<Integer> result = topologicalSort.topologicalSortDfs(vertices, edges);

        assertTrue(result.size() == vertices.size());
        assertEquals(List.of(1, 2, 3, 4), result);
    }
}
