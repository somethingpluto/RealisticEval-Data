/**
 * @brief Calculate the distance between two points on the Earth's surface using the Haversine formula.
 *
 * @param lat1 Latitude of the first point in degrees.
 * @param lon1 Longitude of the first point in degrees.
 * @param lat2 Latitude of the second point in degrees.
 * @param lon2 Longitude of the second point in degrees.
 *
 * @return Distance between the two points in kilometers. The result is a double precision floating-point
 *         number representing the shortest distance over the Earth's surface, accounting for its curvature.
 *
 * @note This implementation assumes the Earth is a perfect sphere, which may introduce slight errors in distance
 *       calculations, especially for long distances. For most practical purposes, the results are sufficiently accurate.
 */
double haversine_distance(double lat1, double lon1, double lat2, double lon2) {}
