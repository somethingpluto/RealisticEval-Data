#include <iostream>
#include <tuple>
#include <cmath>
#include <stdexcept>

// Function to calculate the Euclidean distance between two points in a 2D space.
float calculate_euclidean_distance(const std::tuple<float, float>& point1, const std::tuple<float, float>& point2) {
    // Extract coordinates from the input tuples
    float x1, y1, x2, y2;
    std::tie(x1, y1) = point1;
    std::tie(x2, y2) = point2;

    // Compute differences and Euclidean distance using the Pythagorean theorem
    float dx = x2 - x1;
    float dy = y2 - y1;

    return std::sqrt(dx * dx + dy * dy);
}

int main() {
    try {
        // Example usage
        auto point1 = std::make_tuple(1.0f, 2.0f);
        auto point2 = std::make_tuple(4.0f, 6.0f);

        float distance = calculate_euclidean_distance(point1, point2);
        std::cout << "Euclidean distance: " << distance << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}