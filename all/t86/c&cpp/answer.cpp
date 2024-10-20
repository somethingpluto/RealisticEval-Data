#include <vector>
#include <utility>
#include <cmath>   

std::vector<std::pair<int, int>> bresenham_line(int x1, int y1, int x2, int y2) {
    std::vector<std::pair<int, int>> points;
    int dx = std::abs(x2 - x1);
    int dy = -std::abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx + dy;  // error value e_xy

    while (true) {
        points.push_back(std::make_pair(x1, y1));
        if (x1 == x2 && y1 == y2) {
            break;
        }
        int e2 = 2 * err;
        if (e2 >= dy) {  // e_xy+e_x > 0
            err += dy;
            x1 += sx;
        }
        if (e2 <= dx) {  // e_xy+e_y < 0
            err += dx;
            y1 += sy;
        }
    }

    return points;
}

int main() {
    std::vector<std::pair<int, int>> line_points = bresenham_line(0, 0, 5, 3);
    for (const auto& point : line_points) {
        std::cout << "(" << point.first << ", " << point.second << ")" << std::endl;
    }
    return 0;
}