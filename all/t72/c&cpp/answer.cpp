#include <iostream>
#include <array>

// Function prototype for getting 3D coordinates from 2D pixel coordinates
std::array<double, 3> get_3d_coordinates(const std::array<std::array<double, 3>, 3>& K, double d, double x, double y);

// Implementation of the function
std::array<double, 3> get_3d_coordinates(const std::array<std::array<double, 3>, 3>& K, double d, double x, double y) {
    std::array<double, 3> result;

    // Calculate 3D coordinates
    result[0] = (x - K[0][2]) * d / K[0][0];
    result[1] = (y - K[1][2]) * d / K[1][1];
    result[2] = d;

    return result;
}