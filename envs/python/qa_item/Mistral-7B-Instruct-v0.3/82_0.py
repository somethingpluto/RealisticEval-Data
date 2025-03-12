from typing import List, Dict, Any
import networkx as nx

class Graph:
    def __init__(self, edges):
        self.graph = nx.DiGraph(edges)

    def cycles_by_size(self, filter_repeat_nodes=True) -> Dict[Any, List]:
        cycle_dict = {}

        def find_cycles(node, path, cycle):
            path += (node,)
            if node in cycle:
                if len(path) > len(cycle):
                    cycle_dict[len(path)] = [cycle]
                else:
                    cycle_dict[len(path)] = list(set(cycle) & set(path))
                return

            if filter_repeat_nodes and node in path:
                return

            for neighbor in self.graph.neighbors(node):
                find_cycles(neighbor, path, cycle + path)

        for node in self.graph.nodes():
            find_cycles(node, (node,), ())

        return cycle_dict
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