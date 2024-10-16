# generated by chatgpt
def on_line(point_a, point_b, check_point):
    # Calculate the cross product and dot product
    cross_product = (check_point[1] - point_a[1]) * (point_b[0] - point_a[0]) - (point_b[1] - point_a[1]) * (
                check_point[0] - point_a[0])
    dot_product = (check_point[0] - point_a[0]) * (point_b[0] - point_a[0]) + (check_point[1] - point_a[1]) * (
                point_b[1] - point_a[1])

    # Check if the points are collinear and if check_point is between point_a and point_b
    if abs(cross_product) < 0.001 and dot_product >= 0 and dot_product <= (point_b[0] - point_a[0]) * (
            point_b[0] - point_a[0]) + (point_b[1] - point_a[1]) * (point_b[1] - point_a[1]):
        return True

    return False