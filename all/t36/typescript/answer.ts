type AdjacencyMatrix = (number | Infinity)[][];

function floydWarshallShortestPaths(adjacencyMatrix: AdjacencyMatrix): AdjacencyMatrix {
    const numVertices = adjacencyMatrix.length;

    function recursiveFloydWarshall(k: number): AdjacencyMatrix {
        if (k === numVertices) {
            return adjacencyMatrix;
        }
        for (let i = 0; i < numVertices; i++) {
            for (let j = 0; j < numVertices; j++) {
                adjacencyMatrix[i][j] = Math.min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j]);
            }
        }
        return recursiveFloydWarshall(k + 1);
    }

    return recursiveFloydWarshall(0);
}