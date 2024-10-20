#include <vector>
#include <list>

/**
 * @brief Achieve topological sorting, based on depth priority search
 *
 * @param vertices A vector of integers representing the vertices in the graph.
 *                 Each vertex should be a unique integer.
 * @param edges A vector of pairs of integers where each pair represents a directed
 *              edge in the graph and is formed as (start_vertex, end_vertex).
 *
 * @return A vector of integers representing the vertices in topological order.
 *         If the graph contains a cycle, and thus cannot have a valid topological
 *         ordering, an empty vector is returned.
 */
std::vector<int> topological_sort_dfs(const std::vector<int>& vertices, const std::vector<std::pair<int, int>>& edges);