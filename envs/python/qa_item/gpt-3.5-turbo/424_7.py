import heapq
from typing import Dict

def dijkstra(graph: Dict, start: str) -> Dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
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