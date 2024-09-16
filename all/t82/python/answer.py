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
