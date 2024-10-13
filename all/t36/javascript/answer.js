/**
 * Implements Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
 * in a graph represented by an adjacency matrix.
 *
 * @param {Array<Array<number>>} adjacencyMatrix - The adjacency matrix representing the graph,
 * where adjacencyMatrix[i][j] is the weight of the edge from vertex i to vertex j. If there is
 * no edge, the weight should be represented as Infinity.
 *
 * @returns {Array<Array<number>>} - The matrix representing the shortest paths between all pairs of vertices.
 * shortestPaths[i][j] will hold the shortest distance from vertex i to vertex j.
 */
function floydWarshallShortestPaths(adjacencyMatrix) {
    const numVertices = adjacencyMatrix.length;

    function _recursiveFloydWarshall(k) {
        /**
         * Recursive helper function for Floyd-Warshall algorithm.
         *
         * @param {number} k - The current intermediate vertex being considered.
         *
         * @returns {Array<Array<number>>} - The updated adjacency matrix after considering the current intermediate vertex.
         */
        if (k === numVertices) {
            return adjacencyMatrix;
        }
        for (let i = 0; i < numVertices; i++) {
            for (let j = 0; j < numVertices; j++) {
                // Update the distance to the minimum of the current or via vertex k
                adjacencyMatrix[i][j] = Math.min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j]);
            }
        }
        return _recursiveFloydWarshall(k + 1);
    }

    return _recursiveFloydWarshall(0);
}
