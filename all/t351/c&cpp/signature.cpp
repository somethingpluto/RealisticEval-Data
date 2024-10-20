/**
 * @brief Calculates the value of a cubic Bezier curve at a given parameter t.
 *
 * @param t The parameter value between 0 and 1 that represents a position along the curve.
 * @type t float
 *
 * @param p0 The first control point of the curve, typically where the curve starts.
 * @type p0 float
 *
 * @param p1 The second control point, which influences the tangent at the beginning of the curve.
 * @type p1 float
 *
 * @param p2 The third control point, which influences the tangent at the end of the curve.
 * @type p2 float
 *
 * @param p3 The fourth control point, typically where the curve ends.
 * @type p3 float
 *
 * @return The point on the Bezier curve corresponding to the parameter \( t \).
 * @rtype float
 */

float bezier(float t, float p0, float p1, float p2, float p3) {
    float d = 1 - t;
    return (p0 * d * d * d +
            3 * p1 * d * d * t +
            3 * p2 * d * t * t +
            p3 * t * t * t);
}