package org.real.temp;

import java.util.Arrays;
import java.util.List;

public class Answer {

    public static void main(String[] args) {
        // Example usage
        List<List<Double>> adjacencyMatrix = Arrays.asList(
            Arrays.asList(Double.POSITIVE_INFINITY, 3.0, Double.POSITIVE_INFINITY, 7.0),
            Arrays.asList(2.0, Double.POSITIVE_INFINITY, 5.0, 1.0),
            Arrays.asList(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY),
            Arrays.asList(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, 2.0, Double.POSITIVE_INFINITY)
        );

        List<List<Double>> shortestPaths = floydWarshallShortestPaths(adjacencyMatrix);
        System.out.println(shortestPaths);
    }

    public static List<List<Double>> floydWarshallShortestPaths(List<List<Double>> adjacencyMatrix) {
        int numVertices = adjacencyMatrix.size();

        return _recursiveFloydWarshall(adjacencyMatrix, numVertices, 0);
    }

    private static List<List<Double>> _recursiveFloydWarshall(List<List<Double>> adjacencyMatrix, int numVertices, int k) {
        if (k == numVertices) {
            return adjacencyMatrix;
        }
        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                double viaK = adjacencyMatrix.get(i).get(k) + adjacencyMatrix.get(k).get(j);
                double currentDistance = adjacencyMatrix.get(i).get(j);

                if (currentDistance > viaK) {
                    adjacencyMatrix.get(i).set(j, viaK);
                }
            }
        }
        return _recursiveFloydWarshall(adjacencyMatrix, numVertices, k + 1);
    }
}