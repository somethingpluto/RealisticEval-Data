import { PriorityQueue } from 'typescript-collections';

/**
 * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
 *
 * @param graph - A dictionary representing the adjacency list of the graph. Each key is a node, and the value is a list of tuples (neighbor, weight).
 * @param start - The starting node for the shortest path search.
 * @returns A dictionary with the shortest distance from the start node to each node.
 */
function dijkstra(graph: Record<string, Array<[string, number]>>, start: string): Record<string, number> {
    // Priority queue for the minimum distance nodes
    const queue = new PriorityQueue<[number, string]>((a, b) => a[0] - b[0]);
    // Dictionary to store the shortest path to each node
    const shortestPaths: Record<string, number> = {};
    Object.keys(graph).forEach(node => {
        shortestPaths[node] = Infinity;
    });
    shortestPaths[start] = 0;
    // Push the starting node with distance 0 into the queue
    queue.enqueue([0, start]);

    while (!queue.isEmpty()) {
        const [currentDistance, currentNode] = queue.dequeue()!;

        // If the distance is greater than the recorded shortest path, skip processing
        if (currentDistance > shortestPaths[currentNode]) {
            continue;
        }

        // Explore neighbors
        for (const [neighbor, weight] of graph[currentNode]) {
            const distance = currentDistance + weight;

            // Only consider this new path if it's better
            if (distance < shortestPaths[neighbor]) {
                shortestPaths[neighbor] = distance;
                queue.enqueue([distance, neighbor]);
            }
        }
    }

    return shortestPaths;
}
