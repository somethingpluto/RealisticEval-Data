
class Point {
public:
    double x; // X-coordinate of the point
    double y; // Y-coordinate of the point

    // Constructor for the Point class
    Point(double x, double y) : x(x), y(y) {}

    // Calculate the Euclidean distance to another point
    double distance_to(const Point& other) const;
};
/**
 * @brief Finds the k nearest neighbors to the specified query point.
 *
 * This function identifies the k nearest neighbors to a given query point 
 * from a collection of available points in the space.
 *
 * @param points A list of Point objects representing the available points in the space.
 * @type points std::vector<Point>
 *
 * @param query_point The Point object for which we want to find the nearest neighbors.
 * @type query_point Point
 *
 * @param k The number of nearest neighbors to find.
 * @type k int
 *
 * @return A list of the k nearest Point objects to the query_point.
 * @rtype std::vector<Point>
 */

std::vector<Point> find_k_nearest_neighbors(const std::vector<Point>& points, const Point& query_point, int k);