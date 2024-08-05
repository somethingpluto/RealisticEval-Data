from line_seg_int import intersect_coords


def is_point_in_polygon(polygon: list, point: tuple) -> bool:
    """
    Determines if a point is inside a polygon using the raycasting algorithm.

    Args:
    - polygon: A list of (float, float) tuples representing the vertices of the polygon.
    - point: A (float, float) tuple representing the point to check.

    Returns:
    - bool: True if the point is inside the polygon or on its edge, False otherwise.
    """
    is_inside = False
    x_p, y_p = point
    cast_ray = (point, (float('inf'), y_p))

    # Loop through each pair of vertices, including the wrap-around pair
    for i in range(len(polygon)):
        current_vertex = polygon[i]
        next_vertex = polygon[(i + 1) % len(polygon)]  # Wrap-around using modulo

        if current_vertex == point:
            return True

        # Check for intersection with the ray
        if intersect_coords(cast_ray, (current_vertex, next_vertex)) is not None:
            is_inside = not is_inside

    return is_inside
