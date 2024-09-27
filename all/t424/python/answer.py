import heapq


def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.

    Parameters:
    - graph (dict): A dictionary representing the adjacency list of the graph. Each key is a node, and the value is a list of tuples (neighbor, weight).
    - start: The starting node for the shortest path search.

    Returns:
    - dict: A dictionary with the shortest distance from the start node to each node.
    """
    # Priority queue for the minimum distance nodes
    queue = []
    # Dictionary to store the shortest path to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    # Push the starting node with distance 0 into the queue
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If the distance is greater than the recorded shortest path, skip processing
        if current_distance > shortest_paths[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return shortest_paths