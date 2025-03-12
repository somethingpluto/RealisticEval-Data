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
    graph = {v: [] for v in vertices}
    in_degree = {v: 0 for v in vertices}

    for edge in edges:
        start_vertex, end_vertex = edge
        graph[start_vertex].append(end_vertex)
        in_degree[end_vertex] += 1

    stack = [v for v in vertices if in_degree[v] == 0]
    result = []

    while stack:
        current_vertex = stack.pop()
        result.append(current_vertex)

        for neighbor in graph[current_vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    if len(result) != len(vertices):
        return []
    return result
import unittest


class TestTopologicalSortDFS(unittest.TestCase):
    def test_simple_chain(self):
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3)]
        self.assertEqual(topological_sort_dfs(vertices, edges), [1, 2, 3])


    def test_disconnected_graph(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2)]
        # There are multiple correct answers possible
        result = topological_sort_dfs(vertices, edges)
        self.assertTrue(result.index(1) < result.index(2))
        self.assertTrue(3 in result and 4 in result)

    def test_complex_graph(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (6, 1)]
        result = topological_sort_dfs(vertices, edges)
        self.assertTrue(result.index(1) < result.index(2))
        self.assertTrue(result.index(1) < result.index(3))
        self.assertTrue(result.index(2) < result.index(4))
        self.assertTrue(result.index(3) < result.index(4))
        self.assertTrue(result.index(4) < result.index(5))
        self.assertTrue(result.index(6) < result.index(1))

    def test_single_vertex(self):
        vertices = [1]
        edges = []
        self.assertEqual(topological_sort_dfs(vertices, edges), [1])
if __name__ == '__main__':
    unittest.main()