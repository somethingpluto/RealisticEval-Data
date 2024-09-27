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
