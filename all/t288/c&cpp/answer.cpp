#include <vector>
#include <utility> // for std::pair

std::vector<std::pair<int, int>> bresenhamLine(int x1, int y1, int x2, int y2) {
    std::vector<std::pair<int, int>> linePoints;

    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;

    while (true) {
        linePoints.push_back({x1, y1});

        if (x1 == x2 && y1 == y2)
            break;

        int e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }

    return linePoints;
}