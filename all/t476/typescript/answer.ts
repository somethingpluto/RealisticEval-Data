function topologicalSortDFS(vertices: number[], edges: [number, number][]): number[] {
    /**
     * Achieves topological sorting based on depth-first search (DFS).
     *
     * @param {number[]} vertices - A list of vertices in the graph. Each vertex should be a unique integer.
     * @param {[number, number][]} edges - A list of tuples where each tuple represents a directed edge
     *                                      in the graph and is formed as [start_vertex, end_vertex].
     * @returns {number[]} - A list of vertices in topological order. If the graph contains a cycle,
     *                      and thus cannot have a valid topological ordering, an empty array is returned.
     */
    const graph: Map<number, number[]> = new Map();
    const visited: Set<number> = new Set();
    const result: number[] = [];  // Use an array to store the result

    // Build the graph
    edges.forEach(([u, v]) => {
        if (!graph.has(u)) graph.set(u, []);
        graph.get(u)?.push(v);
    });

    // Recursive depth-first search function
    function dfs(node: number) {
        if (visited.has(node)) return;
        visited.add(node);
        if (graph.has(node)) {
            graph.get(node)?.forEach(neighbor => {
                if (!visited.has(neighbor)) {
                    dfs(neighbor);
                }
            });
        }
        result.unshift(node);  // Add the node to the front of the result array
    }

    // Traverse all nodes
    vertices.forEach(vertex => {
        if (!visited.has(vertex)) {
            dfs(vertex);
        }
    });

    return result;
}