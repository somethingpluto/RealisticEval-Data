#include <iostream>
#include <vector>
#include <cmath>
#include <stdexcept>
#include <limits>

// Function to find the closest element to the target value in a vector of doubles
double find_closest_element(double target, const std::vector<double>& elements) {
    if (elements.empty()) {
        throw std::invalid_argument("The list of elements cannot be empty.");
    }

    // Initialize the closest element with the first element of the vector
    double closest = elements[0];

    // Iterate through the elements to find the closest one
    for (const auto& element : elements) {
        if (std::abs(element - target) < std::abs(closest - target)) {
            closest = element;
        }
    }

    return closest;
}