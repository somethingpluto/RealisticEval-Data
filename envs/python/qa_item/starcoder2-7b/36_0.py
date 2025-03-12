from typing import List, Union

def find_shortest_paths_by_floyd_warshall(adjacency_matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    n = len(adjacency_matrix)
    shortest_paths = [[float('inf') for _ in range(n)] for _ in range(n)]

    # Initialize shortest_paths with the weights of the edges
    for i in range(n):
        for j in range(n):
            shortest_paths[i][j] = adjacency_matrix[i][j]

    # Update shortest_paths using Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])

    return shortest_paths
import unittest

class TestFloydWarshallShortestPaths(unittest.TestCase):
    def test_basic_functionality(self):
        # Basic test.js case with a simple graph
        matrix = [
            [0, 3, float('inf'), 7],
            [8, 0, 2, float('inf')],
            [5, float('inf'), 0, 1],
            [2, float('inf'), float('inf'), 0]
        ]
        expected = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Basic functionality test.js failed")

    def test_single_vertex_graph(self):
        # Test case with a single vertex graph (1x1 matrix)
        matrix = [
            [0]
        ]
        expected = [
            [0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Single vertex graph test.js failed")

    def test_two_vertices_graph(self):
        # Test case with two vertices
        matrix = [
            [0, 1],
            [1, 0]
        ]
        expected = [
            [0, 1],
            [1, 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Two vertices graph test.js failed")

    def test_large_infinite_weights(self):
        # Test case with infinite weights
        matrix = [
            [0, float('inf')],
            [float('inf'), 0]
        ]
        expected = [
            [0, float('inf')],
            [float('inf'), 0]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Large infinite weights test.js failed")

    def test_negative_cycle(self):
        # Test case with a negative cycle
        matrix = [
            [0, 1, float('inf')],
            [float('inf'), 0, -1],
            [-1, float('inf'), 0]
        ]
        expected = [
            [-1, 0, -1],
            [-2, -1, -2],
            [-2, -1, -2]
        ]
        result = find_shortest_paths_by_floyd_warshall(matrix)
        self.assertEqual(result, expected, "Negative cycle test.js failed")



if __name__ == '__main__':
    unittest.main()