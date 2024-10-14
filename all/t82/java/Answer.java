package org.real.temp;

import java.util.*;
import java.util.stream.Collectors;
import org.jgrapht.Graph;
import org.jgrapht.GraphPath;
import org.jgrapht.alg.cycle.SimpleCycleBasis;
import org.jgrapht.alg.cycle.SimpleCycleBasisImpl;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.DirectedPseudograph;

public class Answer {

    private static class Graph {
        private DirectedPseudograph<String, DefaultEdge> graph;

        public Graph(List<List<String>> edges) {
            this.graph = new DirectedPseudograph<>(DefaultEdge.class);
            // Add vertices
            Set<String> vertices = new HashSet<>();
            for (List<String> edge : edges) {
                vertices.add(edge.get(0));
                vertices.add(edge.get(1));
            }
            this.graph.addAllVertices(vertices);

            // Add edges
            for (List<String> edge : edges) {
                this.graph.addEdge(edge.get(0), edge.get(1));
            }
        }

        public Map<Integer, List<Graph>> cyclesBySize(boolean filterRepeatNodes) {
            SimpleCycleBasis<String, DefaultEdge> cycleBasis = new SimpleCycleBasisImpl<>(this.graph);
            List<List<String>> allCycles = cycleBasis.getCycles();

            List<List<String>> cycles = allCycles.stream()
                    .filter(cycle -> cycle.size() > 2)
                    .collect(Collectors.toList());

            if (filterRepeatNodes) {
                cycles = cycles.stream()
                        .filter(cycle -> cycle.size() == new HashSet<>(cycle).size())
                        .collect(Collectors.toList());
            }

            Set<Set<String>> uniqueCycles = cycles.stream()
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new) // Convert to immutable set
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .map(ArrayList::new)
                    .collect(Collectors.toCollection(LinkedHashSet::new));

            Map<Integer, List<Graph>> uniqueCyclesBySize = new LinkedHashMap<>();
            for (Set<String> cycle : uniqueCycles) {
                int size = cycle.size();
                Graph subgraph = new Graph(new ArrayList<>(cycle.stream().flatMap(node -> graph.outgoingEdgesOf(node).stream()
                        .map(edge -> Arrays.asList(node, graph.getEdgeTarget(edge))))
                        .collect(Collectors.toList())));
                uniqueCyclesBySize.computeIfAbsent(size, k -> new ArrayList<>()).add(subgraph);
            }

            return uniqueCyclesBySize;
        }
    }

    public static void main(String[] args) {
        List<List<String>> edges = Arrays.asList(
                Arrays.asList("A", "B"),
                Arrays.asList("B", "C"),
                Arrays.asList("C", "D"),
                Arrays.asList("D", "A"),
                Arrays.asList("E", "F"),
                Arrays.asList("F", "G"),
                Arrays.asList("G", "E")
        );

        Graph graph = new Graph(edges);
        Map<Integer, List<Graph>> cyclesBySize = graph.cyclesBySize(true);
        System.out.println(cyclesBySize);
    }
}