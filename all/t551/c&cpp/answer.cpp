#include <iostream>
#include <vector>
#include <cmath>

std::vector<double> get_mids_from_edges(const std::vector<double>& edges) {
    // Calculate midpoints using vectorized operations
    std::vector<double> mids;
    for (size_t i = 0; i < edges.size() - 1; ++i) {
        double midpoint = (edges[i] + edges[i + 1]) / 2.0;
        mids.push_back(midpoint);
    }

    return mids;
}