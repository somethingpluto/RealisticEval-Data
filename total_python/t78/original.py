def rotation_mapping_to_matrix(rotation_map: dict[int, int]) -> np.ndarray:
    """
    Written by chatGPT
    Convert a rotation map to a rotation matrix.
    """

    # Create a rotation matrix from the rotation map
    rotation_matrix = np.zeros((3, 3))

    for i in range(3):
        # Find the corresponding vector from the mapping
        # Note: we only need to consider vectors with positive first component (1, 3, 5 in RULE_ORDER)
        # Because a rotation is completely determined by where it sends these three vectors
        vector = RULE_ORDER[rotation_map[2 * i + 1]]

        # Add the vector as a column in the rotation matrix
        rotation_matrix[:, i] = vector
    assert np.linalg.det(rotation_matrix) == 1

    # Calculate the quaternion using the function from the previous part
    return rotation_matrix