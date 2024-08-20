import unittest


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

from collections import defaultdict
from typing import List, Dict, Any

import networkx as nx


class Graph:
    def __init__(self, edges):
        self.graph = nx.DiGraph(edges)

    def cycles_by_size(self, filter_repeat_nodes=True) -> Dict[Any,List]:

        all_cycles = list(nx.simple_cycles(self.graph))
        cycles = [cycle for cycle in all_cycles if len(cycle) > 2]
        if filter_repeat_nodes:
            cycles = [cycle for cycle in cycles if len(cycle) == len(set(cycle))]

        unique_cycles = list(set(frozenset(cycle) for cycle in cycles))
        unique_cycles_by_size = defaultdict(list)
        for cycle in unique_cycles:
            size = len(cycle)
            unique_cycles_by_size[size].append(self.graph.subgraph(list(cycle)))

        return unique_cycles_by_size
