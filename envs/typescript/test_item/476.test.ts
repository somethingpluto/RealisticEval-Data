// ... (previous code for context)

function topologicalSortDFS(vertices: number[], edges: [number, number][]): number[] {
  const visited = new Set<number>();
  const stack: number[] = [];
  const graph = buildGraph(vertices, edges);

  for (const vertex of vertices) {
    if (!visited.has(vertex)) {
      if (!dfs(vertex, visited, stack, graph)) {
        return []; // Cycle detected
      }
    }
  }

  return stack.reverse();
}

function buildGraph(vertices: number[], edges: [number, number][]): Map<number, number[]> {
  const graph = new Map<number, number[]>();
  for (const vertex of vertices) {
    graph.set(vertex, []);
  }
  for (const [from, to] of edges) {
    graph.get(from)?.push(to);
  }
  return graph;
}

function dfs(vertex: number, visited: Set<number>, stack: number[], graph: Map<number, number[]>): boolean {
  if (visited.has(vertex)) {
    return false; // Cycle detected
  }
  visited.add(vertex);
  const neighbors = graph.get(vertex);
  if (neighbors) {
    for (const neighbor of neighbors) {
      if (!dfs(neighbor, visited, stack, graph)) {
        return false;
      }
    }
  }
  stack.push(vertex);
  return true;
}

// ... (rest of the code)
describe('TestTopologicalSortDFS', () => {
    it('test_simple_chain', () => {
        const vertices = [1, 2, 3];
        const edges = [[1, 2], [2, 3]];
        expect(topologicalSortDFS(vertices, edges)).toEqual([1, 2, 3]);
    });

    it('test_disconnected_graph', () => {
        const vertices = [1, 2, 3, 4];
        const edges = [[1, 2]];
        const result = topologicalSortDFS(vertices, edges);
        expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
        expect(result).toContain(3);
        expect(result).toContain(4);
    });

    it('test_complex_graph', () => {
        const vertices = [1, 2, 3, 4, 5, 6];
        const edges = [
            [1, 2],
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 5],
            [6, 1]
        ];
        const result = topologicalSortDFS(vertices, edges);
        expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
        expect(result.indexOf(1)).toBeLessThan(result.indexOf(3));
        expect(result.indexOf(2)).toBeLessThan(result.indexOf(4));
        expect(result.indexOf(3)).toBeLessThan(result.indexOf(4));
        expect(result.indexOf(4)).toBeLessThan(result.indexOf(5));
        expect(result.indexOf(6)).toBeLessThan(result.indexOf(1));
    });

    it('test_single_vertex', () => {
        const vertices = [1];
        const edges = [];
        expect(topologicalSortDFS(vertices, edges)).toEqual([1]);
    });
});
