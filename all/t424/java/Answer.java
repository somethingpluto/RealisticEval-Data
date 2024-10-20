package org.real.temp;

import java.util.*;

public class Answer {
    /**
     * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
     *
     * @param graph   A map representing the adjacency list of the graph. Each key is a node, and the value is a list of pairs (neighbor, weight).
     * @param start   The starting node for the shortest path search.
     * @return A map with the shortest distance from the start node to each node.
     */
    public static Map<String, Integer> dijkstra(Map<String, List<Pair<String, Integer>>> graph, String start) {
        // Priority queue for the minimum distance nodes
        PriorityQueue<Pair<Integer, String>> queue = new PriorityQueue<>(Comparator.comparing(Pair::getFirst));

        // Map to store the shortest path to each node
        Map<String, Integer> shortestPaths = new HashMap<>();
        for (String node : graph.keySet()) {
            shortestPaths.put(node, Integer.MAX_VALUE);
        }
        shortestPaths.put(start, 0);

        // Push the starting node with distance 0 into the queue
        queue.offer(new Pair<>(0, start));

        while (!queue.isEmpty()) {
            Pair<Integer, String> currentPair = queue.poll();
            int currentDistance = currentPair.getFirst();
            String currentNode = currentPair.getSecond();

            // If the distance is greater than the recorded shortest path, skip processing
            if (currentDistance > shortestPaths.get(currentNode)) {
                continue;
            }

            // Explore neighbors
            for (Pair<String, Integer> neighborPair : graph.get(currentNode)) {
                String neighbor = neighborPair.getFirst();
                int weight = neighborPair.getSecond();
                int distance = currentDistance + weight;

                // Only consider this new path if it's better
                if (distance < shortestPaths.get(neighbor)) {
                    shortestPaths.put(neighbor, distance);
                    queue.offer(new Pair<>(distance, neighbor));
                }
            }
        }

        return shortestPaths;
    }

    // Utility class to represent a pair of values
    public static class Pair<T1, T2> {
        private T1 first;
        private T2 second;

        public Pair(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }
    }

}