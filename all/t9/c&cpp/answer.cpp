#include <iostream>
#include <vector>

// Function to check whether point C is on the line formed by points A and B
bool is_point_on_line(const std::vector<int>& A, const std::vector<int>& B, const std::vector<int>& C) {
    int x_a = A[0], y_a = A[1];
    int x_b = B[0], y_b = B[1];
    int x_c = C[0], y_c = C[1];

    // Handle the vertical line case where the x-coordinates of points A and B are the same
    if (x_a == x_b) {
        return x_c == x_a;  // C must also have the same x-coordinate
    }

    // Calculate slopes using the formula (y2 - y1) / (x2 - x1)
    // Check if slopes of AC and BC are equal
    return (y_c - y_a) * (x_b - x_a) == (y_b - y_a) * (x_c - x_a);
}