#include <vector>
#include <climits>
#include <iostream>

// Function to implement the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
std::vector<std::vector<int>> floydWarshallShortestPaths(const std::vector<std::vector<int>>& adjacencyMatrix) {
    int numVertices = adjacencyMatrix.size();

    // Helper function for the recursive Floyd-Warshall algorithm
    auto recursiveFloydWarshall = [&adjacencyMatrix, numVertices](int k) -> std::vector<std::vector<int>> {
        if (k == numVertices) {
            return adjacencyMatrix;
        }
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                // Update the distance to the minimum of the current or via vertex k
                adjacencyMatrix[i][j] = std::min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j]);
            }
        }
        return recursiveFloydWarshall(k + 1);
    };

    // Initialize the adjacency matrix with the input values
    std::vector<std::vector<int>> matrix = adjacencyMatrix;

    // Start the recursive function with the initial vertex
    return recursiveFloydWarshall(0);
}

int main() {
    // Example adjacency matrix
    std::vector<std::vector<int>> adjacencyMatrix = {
        {0, 3, INT_MAX, 7},
        {8, 0, 2, INT_MAX},
        {5, INT_MAX, 0, 1},
        {2, INT_MAX, INT_MAX, 0}
    };

    // Compute the shortest paths
    std::vector<std::vector<int>> shortestPaths = floydWarshallShortestPaths(adjacencyMatrix);

    // Print the shortest paths matrix
    for (const auto& row : shortestPaths) {
        for (int val : row) {
            if (val == INT_MAX) {
                std::cout << "INF ";
            } else {
                std::cout << val << " ";
            }
        }
        std::cout << std::endl;
    }

    return 0;
}