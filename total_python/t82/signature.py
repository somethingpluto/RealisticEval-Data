from collections import defaultdict
from typing import List, Dict, Any

import networkx as nx


class Graph:
    def __init__(self, edges):
        self.graph = nx.DiGraph(edges)

    def cycles_by_size(self, filter_repeat_nodes=True) -> Dict[Any, List]:
        """
        find the unique cycles from the graph, classify them according to cycle size, and return a dictionary, the key of which is the cycle size, and the value is a list of cycles of corresponding size. The function also provides an option to filter out loops that visit the same node multiple times and ensure that each loop contains at least three nodes

        Args:
            filter_repeat_nodes (bool): Whether to filter out cycles in which the same node is accessed repeatedly in the same cycle

        Returns:

        """
