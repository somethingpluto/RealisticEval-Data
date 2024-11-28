#include <iostream>
#include <vector>
#include <stdexcept>

double squared_euclidean_distance(const std::vector<double>& vec1, const std::vector<double>& vec2) {
    // Check if the vectors are of the same length
    if (vec1.size() != vec2.size()) {
        throw std::invalid_argument("Vectors must be of the same length");
    }

    double distanceSquared = 0.0;
    // Compute the squared Euclidean distance
    for (size_t i = 0; i < vec1.size(); ++i) {
        double diff = vec1[i] - vec2[i];
        distanceSquared += diff * diff;
    }
    return distanceSquared;
}
