#include <iostream>

struct Rectangle {
    int x1, y1; // Bottom-left corner (x1, y1)
    int x2, y2; // Top-right corner (x2, y2)
};

// Function to calculate the overlap area of two rectangles
int calculateOverlapArea(const Rectangle& rect1, const Rectangle& rect2) {
    // Calculate the coordinates of the overlapping rectangle
    int overlapX1 = std::max(rect1.x1, rect2.x1);
    int overlapY1 = std::max(rect1.y1, rect2.y1);
    int overlapX2 = std::min(rect1.x2, rect2.x2);
    int overlapY2 = std::min(rect1.y2, rect2.y2);

    // Check if there is an overlap
    if (overlapX1 < overlapX2 && overlapY1 < overlapY2) {
        // Calculate the width and height of the overlapping rectangle
        int width = overlapX2 - overlapX1;
        int height = overlapY2 - overlapY1;
        // Calculate and return the area of the overlapping rectangle
        return width * height;
    }

    // If there is no overlap, return 0
    return 0;
}