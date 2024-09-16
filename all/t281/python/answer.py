def squared_euclidean_distance(vec1, vec2):
    """
    Compute the squared Euclidean distance between two vectors.

    Args:
    vec1 (list or tuple): First vector.
    vec2 (list or tuple): Second vector.

    Returns:
    float: Squared Euclidean distance between vec1 and vec2.

    Raises:
    ValueError: If the vectors are of different lengths.
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length")

    distance_squared = sum((a - b) ** 2 for a, b in zip(vec1, vec2))
    return distance_squared