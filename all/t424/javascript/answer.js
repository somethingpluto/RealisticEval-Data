function dijkstra(graph, start) {
    const queue = [];
    // Object to store the shortest path to each node
    const shortestPaths = {};
    for (const node in graph) {
        shortestPaths[node] = Infinity;
    }
    shortestPaths[start] = 0;
    // Push the starting node with distance 0 into the queue
    queue.push({ distance: 0, node: start });
    queue.sort((a, b) => a.distance - b.distance);

    while (queue.length > 0) {
        // Extract the node with the smallest distance
        let current = queue.shift();
        let currentDistance = current.distance;
        let currentNode = current.node;

        // If the distance is greater than the recorded shortest path, skip processing
        if (currentDistance > shortestPaths[currentNode]) {
            continue;
        }

        // Explore neighbors
        for (const neighborInfo of graph[currentNode]) {
            const neighbor = neighborInfo.neighbor;
            const weight = neighborInfo.weight;
            const distance = currentDistance + weight;

            // Only consider this new path if it's better
            if (distance < shortestPaths[neighbor]) {
                shortestPaths[neighbor] = distance;
                // Add or update the neighbor in the priority queue
                const indexToUpdate = queue.findIndex(item => item.node === neighbor);
                if (indexToUpdate !== -1) {
                    queue[indexToUpdate].distance = distance;
                    queue.sort((a, b) => a.distance - b.distance);
                } else {
                    queue.push({ distance, node: neighbor });
                    queue.sort((a, b) => a.distance - b.distance);
                }
            }
        }
    }

    return shortestPaths;
}