from line_seg_int import intersect_coords

def is_in_shape(shape: list, point: tuple) -> bool:
    # Takes an input of form:
    # ([(float, float), ...], (float, float))
    # ([(x_1,   x_2  ), ...], (x_p,   y_p  ))
    # Where shape is a list of vertices as tuples

    # Returns True is the point lies within the shape or on its edge, False otherwise
    # Uses a raycasting algorithm and my line_seg_int module

    is_inside = False
    x_p, y_p = point
    cast_ray = (point, (float("inf"), y_p))

    for v, vertex in enumerate(shape):
        # Checking each line segment
        if vertex == point:
            return True
        if v == 0:
            x_1, y_1 = vertex
        else:
            x_2, y_2 = vertex
            # Checking whether a ray cast to the right intersects with the line segment
            if intersect_coords(cast_ray, ((x_1, y_1), (x_2, y_2))) is not None:
                # intersects
                is_inside = not is_inside # Odd number of intersections = inside shape
            x_1, y_1 = x_2, y_2

    return is_inside
