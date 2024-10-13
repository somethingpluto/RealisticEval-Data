def find_t_for_x(target_x, p0, p1, p2):
    """
    Find the parameter t corresponding to a given x-coordinate target_x
    on a quadratic Bézier curve defined by control points p0, p1, and p2.
    
    :param target_x: The x-coordinate for which we want to find the corresponding parameter t.
    :param p0: The first control point of the Bézier curve.
    :param p1: The second control point of the Bézier curve.
    :param p2: The third control point of the Bézier curve.
    :return: The parameter t (in the range [0, 1]) for which the Bézier curve
                evaluated at t is closest to target_x.
    """
    t0 = 0.0
    t1 = 1.0
    tolerance = 1e-6
    max_iterations = 100
    
    x0 = bezier_curve(t0, p0, p1, p2) - target_x
    x1 = bezier_curve(t1, p0, p1, p2) - target_x
    
    for _ in range(max_iterations):
        if abs(x1 - x0) < tolerance:
            break
        
        t2 = t1 - x1 * (t1 - t0) / (x1 - x0)
        x2 = bezier_curve(t2, p0, p1, p2) - target_x
        
        if abs(x2) < tolerance:
            return t2
        
        t0, x0, t1, x1 = t1, x1, t2, x2
    
    return t1  # Return the best approximation found

def bezier_curve(t, p0, p1, p2):
    """
    Calculate the value of the Bézier curve at parameter t.
    
    :param t: Parameter for the Bézier curve (0 <= t <= 1).
    :param p0: The first control point of the Bézier curve.
    :param p1: The second control point of the Bézier curve.
    :param p2: The third control point of the Bézier curve.
    :return: The value of the Bézier curve at t.
    """
    one_minus_t = 1 - t
    return (one_minus_t ** 2) * p0 + (2 * one_minus_t * t) * p1 + (t ** 2) * p2