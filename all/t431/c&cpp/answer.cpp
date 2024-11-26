#include <iostream>
#include <tuple>

// Function to determine if two rectangles intersect horizontally
bool intersect_horizontally(const std::tuple<int, int, int, int>& rect1, const std::tuple<int, int, int, int>& rect2) {
    // Extracting coordinates from tuples
    int x1_1, y1_1, x2_1, y2_1;
    std::tie(x1_1, y1_1, x2_1, y2_1) = rect1;

    int x1_2, y1_2, x2_2, y2_2;
    std::tie(x1_2, y1_2, x2_2, y2_2) = rect2;

    // Check if rectangles intersect horizontally
    return !(x2_1 < x1_2 || x2_2 < x1_1);
}