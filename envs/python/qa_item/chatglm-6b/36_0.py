
from typing import List, Union

def find_shortest_paths_by_floyd_warshall(adjacency_matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implements Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
    in a graph represented by an adjacency matrix.

    Args:
        adjacency_matrix (List[List[Union[int, float]]]): The adjacency matrix representing the graph,
        where adjacency_matrix[i][j] is the weight of the edge from vertex i to vertex j. If there is
        no edge, the weight should be represented as float('inf').

    Returns:
        List[List[Union[int, float]]]: The matrix representing the shortest paths between all pairs of vertices.
        shortest_paths[i][j] will hold the shortest distance from vertex i to vertex j.
    """

    # Initialize the matrix to all zeros
    shortest_paths = [float('inf')] * len(adjacency_matrix)

    # Initialize the index of the first vertex to 0
    first_vertex = 0

    # Initialize the index of the last vertex to len(adjacency_matrix) - 1
    last_vertex = len(adjacency_matrix) - 1

    # Loop through all pairs of vertices
    for i in range(first_vertex, last_vertex):
        for j in range(i + 1, last_vertex):
            # Calculate the weight of the edge from vertex i to vertex j
            weight = adjacency_matrix[i][j]

            # Update the shortest path matrix
            shortest_paths[i][j] = min(shortest_paths[i][j], weight)

            # Update the index of the first vertex
            first_vertex += 1

            # Update the index of the last vertex
            last_vertex -= 1

    # Return the matrix of shortest paths
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