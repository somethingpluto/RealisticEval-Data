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
        result = floyd_warshall_shortest_paths(matrix)
        self.assertEqual(result, expected, "Basic functionality test.js failed")

    def test_single_vertex_graph(self):
        # Test case with a single vertex graph (1x1 matrix)
        matrix = [
            [0]
        ]
        expected = [
            [0]
        ]
        result = floyd_warshall_shortest_paths(matrix)
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
        result = floyd_warshall_shortest_paths(matrix)
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
        result = floyd_warshall_shortest_paths(matrix)
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
        result = floyd_warshall_shortest_paths(matrix)
        self.assertEqual(result, expected, "Negative cycle test.js failed")



from typing import List, Union

def floyd_warshall_shortest_paths(adjacency_matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
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

    num_vertices = len(adjacency_matrix)

    def _recursive_floyd_warshall(k: int) -> List[List[Union[int, float]]]:
        """
        Recursive helper function for Floyd-Warshall algorithm.

        Args:
            k (int): The current intermediate vertex being considered.

        Returns:
            List[List[Union[int, float]]]: The updated adjacency matrix after considering the current intermediate vertex.
        """
        if k == num_vertices:
            return adjacency_matrix
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance to the minimum of the current or via vertex k
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j],
                                             adjacency_matrix[i][k] + adjacency_matrix[k][j])
        return _recursive_floyd_warshall(k + 1)

    return _recursive_floyd_warshall(0)

