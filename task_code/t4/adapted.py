def check_point_on_the_line(point_a: tuple, point_b: tuple, check_point: tuple) -> bool:
    dot_product = (check_point[0] - point_a[0]) * (point_b[0] - point_a[0]) + (check_point[1] - point_a[1]) * (
            point_b[1] - point_a[1])
    squared_length_ab = (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2
    return 0 <= dot_product <= squared_length_ab
