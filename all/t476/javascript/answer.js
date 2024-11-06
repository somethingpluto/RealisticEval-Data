function topologicalSortDFS(vertices, edges) {
    /**
     * Achieve topological sorting based on depth-first search (DFS).
     *
     * @param {Array<number>} vertices - A list of vertices in the graph. Each vertex should be a unique integer.
     * @param {Array<[number, number]>} edges - A list of tuples where each tuple represents a directed edge
     *                                          in the graph and is formed as [start_vertex, end_vertex].
     * @returns {Array<number>} - A list of vertices in topological order. If the graph contains a cycle,
     *                            and thus cannot have a valid topological ordering, an empty array is returned.
     */
    const graph = new Map();
    const visited = new Set();
    const result = [];  // Use an array to store the result

    // Build the graph
    edges.forEach(([u, v]) => {
        if (!graph.has(u)) graph.set(u, []);
        graph.get(u).push(v);
    });

    // Recursive depth-first search function
    function dfs(node) {
        if (visited.has(node)) return;
        visited.add(node);
        if (graph.has(node)) {
            graph.get(node).forEach(neighbor => {
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