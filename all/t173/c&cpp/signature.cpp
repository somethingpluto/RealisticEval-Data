/**
 * Calculate the coordinates of a cubic Bézier curve at a given parameter t (typically between 0 and 1).
 * @param t  A double representing the parameter along the curve, where 0 <= t <= 1.
 * @param p0 A std::array of size 2 representing the x and y coordinates of the start point.
 * @param p1 A std::array of size 2 representing the x and y coordinates of the first control point.
 * @param p2 A std::array of size 2 representing the x and y coordinates of the second control point.
 * @param p3 A std::array of size 2 representing the x and y coordinates of the end point.
 * @return   A std::array of size 2 containing the x and y coordinates of the point on the curve corresponding to the parameter t.
 */
std::array<double, 2> cubicBezier(double t, const std::array<double, 2>& p0, 
                                   const std::array<double, 2>& p1, 
                                   const std::array<double, 2>& p2, 
                                   const std::array<double, 2>& p3) {}