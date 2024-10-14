function topologicalSortDFS(vertices, edges) {
    const adjList = new Map();
    const visited = new Set();
    const stack = [];

    // Initialize adjacency list
    for (const vertex of vertices) {
        adjList.set(vertex, []);
    }

    // Build adjacency list
    for (const [from, to] of edges) {
        adjList.get(from).push(to);
    }

    // DFS traversal
    function dfs(vertex) {
        if (!visited.has(vertex)) {
            visited.add(vertex);

            for (const neighbor of adjList.get(vertex)) {
                dfs(neighbor);
            }

            stack.push(vertex);
        }
    }

    // Perform DFS for all vertices
    for (const vertex of vertices) {
        dfs(vertex);
    }

    return stack.reverse();
}
