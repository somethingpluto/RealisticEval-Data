from typing import List, Tuple


def topological_sort_dfs(vertices: List[int], edges: List[Tuple]) -> List:
    """
    achieve topological sorting, based on depth priority search

    Args:
        vertices (List[int]): A list of vertices in the graph. Each vertex should be a unique integer.
        edges (List[Tuple[int, int]]): A list of tuples where each tuple represents a directed edge
                                       in the graph and is formed as (start_vertex, end_vertex).

    Returns:
        List[int]: A list of vertices in topological order. If the graph contains a cycle,
                   and thus cannot have a valid topological ordering, an empty list is returned.
    """