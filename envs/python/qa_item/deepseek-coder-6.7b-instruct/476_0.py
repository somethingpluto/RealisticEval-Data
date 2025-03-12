from typing import List, Tuple

def topological_sort_dfs(vertices: List[int], edges: List[Tuple[int, int]]) -> List[int]:
    # Create a graph representation using adjacency lists
    graph = {v: [] for v in vertices}
    for start, end in edges:
        graph[start].append(end)
    
    # Initialize the necessary data structures
    visited = set()
    stack = []
    cycle_detected = False
    
    def dfs(vertex):
        nonlocal cycle_detected
        if cycle_detected:
            return
        
        # Mark the current node as visited and part of the recursion stack
        visited.add(vertex)
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor not in stack:
                # If we encounter a node that is already in the visited set but not in the stack,
                # it means we have found a cycle
                cycle_detected = True
        
        # Push the current vertex to the stack which stores the result
        stack.append(vertex)
    
    # Call the recursive helper function to store Topological Sort starting from all vertices one by one
    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)
    
    # If a cycle was detected, return an empty list
    if cycle_detected:
        return []
    
    # The stack now contains the vertices in topological order
    return stack[::-1]
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