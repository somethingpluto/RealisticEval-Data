// Start of the TypeScript code
import { Graph } from 'graphlib';

function floydWarshallShortestPaths(graph: Graph): { distances: number[][], predecessors: number[][] } {
  const distances: number[][] = [];
  const predecessors: number[][] = [];

  // Initialize distances and predecessors matrices
  graph.nodes().forEach((nodeA) => {
    distances[nodeA] = [];
    predecessors[nodeA] = [];
    graph.nodes().forEach((nodeB) => {
      distances[nodeA][nodeB] = graph.edge(nodeA, nodeB) || Infinity;
      predecessors[nodeA][nodeB] = nodeB === Infinity ? -1 : nodeB;
    });
    distances[nodeA][nodeA] = 0;
  });

  // Floyd-Warshall algorithm
  graph.nodes().forEach((k) => {
    graph.nodes().forEach((i) => {
      graph.nodes().forEach((j) => {
        if (distances[i][k] + distances[k][j] < distances[i][j]) {
          distances[i][j] = distances[i][k] + distances[k][j];
          predecessors[i][j] = predecessors[i][k];
        }
      });
    });
  });

  return { distances, predecessors };
}
// End of the TypeScript code
describe('TestFloydWarshallShortestPaths', () => {
    it('test basic functionality', () => {
        // Basic test case with a simple graph
        const matrix = [
            [0, 3, Infinity, 7],
            [8, 0, 2, Infinity],
            [5, Infinity, 0, 1],
            [2, Infinity, Infinity, 0]
        ];
        const expected = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test single vertex graph', () => {
        // Test case with a single vertex graph (1x1 matrix)
        const matrix = [
            [0]
        ];
        const expected = [
            [0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test two vertices graph', () => {
        // Test case with two vertices
        const matrix = [
            [0, 1],
            [1, 0]
        ];
        const expected = [
            [0, 1],
            [1, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test large infinite weights', () => {
        // Test case with infinite weights
        const matrix = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const expected = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test negative cycle', () => {
        // Test case with a negative cycle
        const matrix = [
            [0, 1, Infinity],
            [Infinity, 0, -1],
            [-1, Infinity, 0]
        ];
        const expected = [
            [-1, 0, -1],
            [-2, -1, -2],
            [-2, -1, -2]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });
});
