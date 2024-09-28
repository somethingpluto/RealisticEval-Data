#include <iostream>
#include <cmath>
#include <stdexcept>
#include <tuple>

using namespace std;

// Define a type alias for a point to match the Tuple[float, float] type in Python
using Point = tuple<float, float>;

float calculate_euclidean_distance(const Point& point1, const Point& point2) {
    // Extract coordinates from the input tuples
    float x1, y1, x2, y2;
    tie(x1, y1) = point1;
    tie(x2, y2) = point2;

    // Compute differences and Euclidean distance using the Pythagorean theorem
    float dx = x2 - x1;
    float dy = y2 - y1;

    return sqrt(dx * dx + dy * dy);
}

int main() {
    try {
        Point point1 = {3.0f, 4.0f};
        Point point2 = {0.0f, 0.0f};

        float distance = calculate_euclidean_distance(point1, point2);
        cout << "The Euclidean distance between the points is " << distance << endl;
    }
    catch (const invalid_argument& e) {
        cerr << e.what() << endl;
        return 1;
    }

    return 0;
}