from typing import List, Union

def floyd_warshall_shortest_paths(adjacency_matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implements Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
    in a graph represented by an adjacency matrix.

    Args:
        adjacency_matrix (List[List[Union[int, float]]]): The adjacency matrix representing the graph,
        where adjacency_matrix[i][j] is the weight of the edge from vertex i to vertex j. If there is
        no edge, the weight should be represented as float('inf').

    Returns:
        List[List[Union[int, float]]]: The matrix representing the shortest paths between all pairs of vertices.
        shortest_paths[i][j] will hold the shortest distance from vertex i to vertex j.
    """