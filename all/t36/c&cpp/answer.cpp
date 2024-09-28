#include <iostream>
#include <vector>
#include <limits>

using namespace std;

// Use the largest finite value representable by a float point as infinity
const double INF = numeric_limits<double>::infinity();

// This function implements the recursive part of the Floyd-Warshall algorithm
vector<vector<double>> recursiveFloydWarshall(vector<vector<double>>& adjacencyMatrix, int k, int numVertices) {
    // Base case: if k equals the number of vertices, return the current matrix
    if (k == numVertices) {
        return adjacencyMatrix;
    }

    // Update the matrix considering the k-th vertex as an intermediate vertex
    for (int i = 0; i < numVertices; ++i) {
        for (int j = 0; j < numVertices; ++j) {
            adjacencyMatrix[i][j] = min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j]);
        }
    }

    // Recur for the next vertex
    return recursiveFloydWarshall(adjacencyMatrix, k + 1, numVertices);
}

// This function initiates the Floyd-Warshall algorithm
vector<vector<double>> floydWarshallShortestPaths(vector<vector<double>>& adjacencyMatrix) {
    int numVertices = adjacencyMatrix.size();
    return recursiveFloydWarshall(adjacencyMatrix, 0, numVertices);
}

int main() {
    // Example usage:
    // Graph represented as an adjacency matrix
    vector<vector<double>> adjacencyMatrix = {
        {0, 3, INF, INF},
        {2, 0, INF, 1},
        {INF, 7, 0, 2},
        {INF, INF, 3, 0}
    };

    vector<vector<double>> shortestPaths = floydWarshallShortestPaths(adjacencyMatrix);

    // Print the shortest path matrix
    for (const auto& row : shortestPaths) {
        for (double weight : row) {
            if(weight == INF) {
                cout << "INF ";
            } else {
                cout << weight << " ";
            }
        }
        cout << endl;
    }
    return 0;
}