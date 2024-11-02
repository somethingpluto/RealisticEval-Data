#include <vector>
#include <climits>
#include <iostream>

std::vector<std::vector<int>> floyd_warshall_shortest_paths(const std::vector<std::vector<int>>& adjacencyMatrix) {
    int numVertices = adjacencyMatrix.size();
    
    // Create a copy of the adjacency matrix to modify
    std::vector<std::vector<int>> distance = adjacencyMatrix;

    // Run the Floyd-Warshall algorithm
    for (int k = 0; k < numVertices; ++k) {
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                if (distance[i][k] != INT_MAX && distance[k][j] != INT_MAX) { // Avoid overflow
                    distance[i][j] = std::min(distance[i][j], distance[i][k] + distance[k][j]);
                }
            }
        }
    }
    return distance;
}