def calculate_euclidean_distance(point1, point2):
    # Extract coordinates from the input tuples
    x1, y1 = point1
    x2, y2 = point2

    # Compute differences and Euclidean distance using Pythagorean theorem
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** 0.5
