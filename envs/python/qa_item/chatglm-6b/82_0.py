
from typing import List, Dict, Any
import networkx as nx

class Graph:
    def __init__(self, edges):
        self.graph = nx.DiGraph(edges)

    def cycles_by_size(self, filter_repeat_nodes=True) -> Dict[Any, List]:
        """
        Finds all unique cycles in the graph that are larger than size 2, optionally filtering out cycles with repeated nodes.

        Args:
            filter_repeat_nodes (bool): If True, filters out cycles where any node appears more than once.

        Returns:
            Dict[int, List[nx.Graph]]: A dictionary mapping each cycle size to a list of subgraph objects representing
                each unique cycle of that size.
        """
        # Create a dictionary to store the subgraph objects for each cycle size
        subgraph_dict = {}

        # Create a list to store the subgraph objects for each cycle size
        cycle_list = []

        # Loop through all nodes in the graph
        for node in self.graph.nodes:
            # If the node is a cycle node, add it to the cycle list
            if node in subgraph_dict:
                cycle_list.append(subgraph_dict[node])
            # If the node is not a cycle node, add it to the cycle dictionary
            else:
                subgraph_dict[node] = cycle_list

        # Return the dictionary with the cycle sizes and the list of subgraph objects
        return { cycle_size: cycle_list for cycle_size in range(1, len(cycle_list)) if cycle_list }

import unittest
from collections import defaultdict


class TestGraphCycles(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph([])
        self.assertEqual(g.cycles_by_size(), defaultdict(list),
                         "Failed: Expected an empty defaultdict for an empty graph.")

    def test_graph_no_cycles(self):
        g = Graph([(1, 2), (2, 3)])
        self.assertEqual(g.cycles_by_size(), defaultdict(list),
                         "Failed: Expected an empty defaultdict for a graph with no cycles.")

    def test_simple_cycles(self):
        g = Graph([(1, 2), (2, 3), (3, 1)])
        results = g.cycles_by_size()
        self.assertEqual(len(results[3]), 1, "Failed: Expected one cycle of length 3.")
        self.assertIn(list(results[3][0].nodes()), [[1, 2, 3]], "Failed: Expected cycle nodes to match.")

    def test_multiple_cycles(self):
        g = Graph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1)])
        results = g.cycles_by_size()
        self.assertEqual(len(results[3]), 1, "Failed: Expected one cycle of length 3.")
        self.assertEqual(len(results[4]), 1, "Failed: Expected one cycle of length 4.")

if __name__ == '__main__':
    unittest.main()