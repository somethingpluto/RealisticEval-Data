/**
 * Achieves topological sorting based on depth-first search (DFS).
 *
 * @param {Array<number>} vertices - A list of vertices in the graph. Each vertex should be a unique integer.
 * @param {Array<[number, number]>} edges - A list of tuples where each tuple represents a directed edge
 *                                          in the graph and is formed as [start_vertex, end_vertex].
 * @returns {Array<number>} - A list of vertices in topological order. If the graph contains a cycle,
 *                            and thus cannot have a valid topological ordering, an empty array is returned.
 */
function topologicalSortDFS(vertices, edges) {
    // Create an adjacency list from the edges
    const adjacencyList = {};
    vertices.forEach(vertex => adjacencyList[vertex] = []);
    edges.forEach(([start, end]) => adjacencyList[start].push(end));

    // Arrays to keep track of the state of each vertex
    const visited = new Array(vertices.length).fill(false);
    const departure = new Array(vertices.length).fill(-1);
    let time = 0;
    const topoOrder = [];

    // Helper function to perform DFS
    function dfs(vertex) {
        visited[vertex] = true;
        for (const neighbor of adjacencyList[vertex]) {
            if (!visited[neighbor]) {
                if (!dfs(neighbor)) {
                    return false; // Cycle detected
                }
            } else if (departure[neighbor] === -1) {
                return false; // Back edge detected, indicating a cycle
            }
        }
        // Record the departure time
        departure[vertex] = time++;
        topoOrder.push(vertex);
        return true;
    }

    // Perform DFS on each unvisited vertex
    for (const vertex of vertices) {
        if (!visited[vertex]) {
            if (!dfs(vertex)) {
                return []; // Cycle detected, return empty array
            }
        }
    }

    // Reverse the order to get the topological sort
    return topoOrder.reverse();
}
describe('TestTopologicalSortDFS', () => {
    describe('test_simple_chain', () => {
        it('should sort a simple chain correctly', () => {
            const vertices = [1, 2, 3];
            const edges = [[1, 2], [2, 3]];
            expect(topologicalSortDFS(vertices, edges)).toEqual([1, 2, 3]);
        });
    });

    describe('test_disconnected_graph', () => {
        it('should handle a disconnected graph correctly', () => {
            const vertices = [1, 2, 3, 4];
            const edges = [[1, 2]];
            const result = topologicalSortDFS(vertices, edges);

            expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
            expect(result.includes(3) && result.includes(4)).toBeTruthy();
        });
    });

    describe('test_complex_graph', () => {
        it('should handle a complex graph correctly', () => {
            const vertices = [1, 2, 3, 4, 5, 6];
            const edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [6, 1]];
            const result = topologicalSortDFS(vertices, edges);

            expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
            expect(result.indexOf(1)).toBeLessThan(result.indexOf(3));
            expect(result.indexOf(2)).toBeLessThan(result.indexOf(4));
            expect(result.indexOf(3)).toBeLessThan(result.indexOf(4));
            expect(result.indexOf(4)).toBeLessThan(result.indexOf(5));
            expect(result.indexOf(6)).toBeLessThan(result.indexOf(1));
        });
    });

    describe('test_single_vertex', () => {
        it('should handle a single vertex correctly', () => {
            const vertices = [1];
            const edges = [];
            expect(topologicalSortDFS(vertices, edges)).toEqual([1]);
        });
    });
});
