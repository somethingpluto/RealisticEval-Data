#include <vector>
#include <cmath>

int squaredEuclideanDistance(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    if (vec1.size() != vec2.size()) {
        throw std::invalid_argument("Vectors must have the same size");
    }

    int sum = 0;
    for (size_t i = 0; i < vec1.size(); ++i) {
        int diff = vec1[i] - vec2[i];
        sum += diff * diff;
    }
    return sum;
}