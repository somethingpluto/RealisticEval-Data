
import heapq
from typing import Dict

def dijkstra(graph: Dict, start: str) -> Dict:
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
    Args:
        graph(Dict): A dictionary representing the adjacency list of the graph. Each key is a node, and the value is a list of tuples (neighbor, weight).
        start(str): The starting node for the shortest path search.

    Returns:
        Dict: A dictionary with the shortest distance from the start node to each node.
    """

    # Initialize the heap to store the distances
    heap = [(0, 0)]

    # Iterate over the nodes in the graph
    for node, neighbors in graph.items():
        # Iterate over the neighbors and calculate the distance
        for neighbor, weight in neighbors.items():
            heapq.heappush(heap, (distance, weight))
            distance += weight

    # Iterate over the nodes in the heap and return the shortest distance
    return heapq.heappop(heap)

import unittest

class TestDijkstraAlgorithm(unittest.TestCase):

    def setUp(self):
        # Sample graphs for testing
        self.graph1 = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)],
        }

        self.graph2 = {
            'A': [('B', 2)],
            'B': [('A', 2), ('C', 3)],
            'C': [('B', 3), ('D', 1)],
            'D': [('C', 1)],
        }

        self.graph_with_isolated_node = {
            'A': [('B', 1)],
            'B': [('A', 1)],
            'C': [],  # Isolated node
        }

        self.graph_with_negative_weight = {
            'A': [('B', 2), ('C', 1)],
            'B': [('D', 3)],
            'C': [('B', -1), ('D', 4)],
            'D': [],
        }

    def test_shortest_paths_graph1(self):
        """Test shortest paths in a normal graph."""
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
        result = dijkstra(self.graph1, 'A')
        self.assertEqual(result, expected)

    def test_shortest_paths_graph2(self):
        """Test shortest paths in a different normal graph."""
        expected = {'A': 0, 'B': 2, 'C': 5, 'D': 6}
        result = dijkstra(self.graph2, 'A')
        self.assertEqual(result, expected)

    def test_shortest_paths_with_isolated_node(self):
        """Test shortest paths with an isolated node."""
        expected = {'A': 0, 'B': 1, 'C': float('inf')}
        result = dijkstra(self.graph_with_isolated_node, 'A')
        self.assertEqual(result, expected)


    def test_starting_at_isolated_node(self):
        """Test when starting at an isolated node."""
        expected = {'C': 0, 'A': float('inf'), 'B': float('inf')}
        result = dijkstra(self.graph_with_isolated_node, 'C')
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()