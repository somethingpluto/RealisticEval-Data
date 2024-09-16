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
