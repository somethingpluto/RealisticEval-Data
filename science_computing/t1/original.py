def on_line(point_a: tuple, point_b: tuple, check_point: tuple) -> bool:
    cross_product = (check_point[1] - point_a[1]) * (point_b[0] - point_a[0]) - (point_b[1] - point_a[1]) * (
            check_point[0] - point_a[0])
    dot_product = (check_point[0] - point_a[0]) * (point_b[0] - point_a[0]) + (check_point[1] - point_a[1]) * (
            point_b[1] - point_a[1])

    if abs(cross_product) < 0.001 and 0 <= dot_product <= (point_b[0] - point_a[0]) * (
            point_b[0] - point_a[0]) + (point_b[1] - point_a[1]) * (point_b[1] - point_a[1]):
        return True

    return False
