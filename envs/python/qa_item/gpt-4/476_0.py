from typing import List, Tuple

def topological_sort_dfs(vertices: List[int], edges: List[Tuple]) -> List:
    def dfs(vertex, visited, stack):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(vertex)
    
    graph = {v: [] for v in vertices}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    visited = {v: False for v in vertices}
    stack = []
    
    for vertex in vertices:
        if not visited[vertex]:
            dfs(vertex, visited, stack)
    
    return stack[::-1] if len(stack) == len(vertices) else []
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