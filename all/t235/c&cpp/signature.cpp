/**
 * @brief Calculates the azimuth between two points on the Earth.
 *
 * @param lat1 The latitude of the starting point in decimal degrees.
 * @param lon1 The longitude of the starting point in decimal degrees.
 * @param lat2 The latitude of the ending point in decimal degrees.
 * @param lon2 The longitude of the ending point in decimal degrees.
 *
 * @return The bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
 */
double calculate_bearing(double lat1, double lon1, double lat2, double lon2);
