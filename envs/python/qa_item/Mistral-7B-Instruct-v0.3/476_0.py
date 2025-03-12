from collections import defaultdict
from typing import List, Tuple

def topological_sort_dfs(vertices: List[int], edges: List[Tuple[int, int]]) -> List[int]:
    in_degree = defaultdict(int)
    graph = defaultdict(list)

    for vertex, neighbor in edges:
        in_degree[vertex] += 1
        graph[neighbor].append(vertex)

    zero_in_degree = [vertex for vertex in vertices if in_degree[vertex] == 0]

    sorted_vertices = []
    for vertex in zero_in_degree:
        stack = [vertex]
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        stack.append(neighbor)
        if not stack:
            sorted_vertices += sorted(visited)

    if not sorted_vertices:
        return []

    return sorted_vertices
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