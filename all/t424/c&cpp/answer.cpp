#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <climits>

using namespace std;

// Custom comparator for the priority queue to ensure min-heap behavior
struct Compare {
    bool operator()(pair<int, char> const &a, pair<int, char> const &b) {
        return a.first > b.first;
    }
};

void dijkstra(const unordered_map<char, vector<pair<char, int>>> &graph, char start) {
    /**
     * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
     *
     * Parameters:
     * - graph (unordered_map<char, vector<pair<char, int>>>): A map representing the adjacency list of the graph. Each key is a node, and the value is a vector of pairs (neighbor, weight).
     * - start: The starting node for the shortest path search.
     *
     * Returns:
     * - unordered_map<char, int>: A map with the shortest distance from the start node to each node.
     */

    // Priority queue for the minimum distance nodes
    priority_queue<pair<int, char>, vector<pair<int, char>>, Compare> queue;

    // Map to store the shortest path to each node
    unordered_map<char, int> shortest_paths;

    // Initialize distances to infinity
    for (const auto &entry : graph) {
        shortest_paths[entry.first] = INT_MAX;
    }

    // Set the distance to the start node to 0
    shortest_paths[start] = 0;

    // Push the starting node with distance 0 into the queue
    queue.push({0, start});

    while (!queue.empty()) {
        int current_distance = queue.top().first;
        char current_node = queue.top().second;
        queue.pop();

        // If the distance is greater than the recorded shortest path, skip processing
        if (current_distance > shortest_paths[current_node]) {
            continue;
        }

        // Explore neighbors
        for (const auto &neighbor_info : graph.at(current_node)) {
            char neighbor = neighbor_info.first;
            int weight = neighbor_info.second;

            int distance = current_distance + weight;

            // Only consider this new path if it's better
            if (distance < shortest_paths[neighbor]) {
                shortest_paths[neighbor] = distance;
                queue.push({distance, neighbor});
            }
        }
    }

    // Print the shortest paths
    for (const auto &entry : shortest_paths) {
        cout << "Shortest path to " << entry.first << ": " << entry.second << endl;
    }
}