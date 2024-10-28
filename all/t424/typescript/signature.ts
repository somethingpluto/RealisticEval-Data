/**
 * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
 * 
 * @param graph - A dictionary representing the adjacency list of the graph. Each key is a node, and the value is a list of tuples (neighbor, weight).
 * @param start - The starting node for the shortest path search.
 * @returns A dictionary with the shortest distance from the start node to each node.
 */
function dijkstra(graph: Record<string, Array<[string, number]>>, start: string): Record<string, number> {}