#include <iostream>
#include <vector>
#include <cmath>

// Function to calculate midpoints from a given vector of edges
std::vector<double> getMidsFromEdges(const std::vector<double>& edges) {
    // Calculate midpoints using vectorized operations
    std::vector<double> mids;
    for (size_t i = 0; i < edges.size() - 1; ++i) {
        double midpoint = (edges[i] + edges[i + 1]) / 2.0;
        mids.push_back(midpoint);
    }

    return mids;
}

int main() {
    // Example usage
    std::vector<double> edges = {1.0, 3.0, 5.0, 7.0};
    std::vector<double> mids = getMidsFromEdges(edges);

    // Print the midpoints
    for (const auto& mid : mids) {
        std::cout << mid << " ";
    }
    std::cout << std::endl;

    return 0;
}