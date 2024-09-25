def get_rotation(matrix: 'rai.typing.Affine') -> float:
    """
    Given an affine matrix, return the corresponding rotation
    Written by ChatGPT
    """
    return float(np.arctan2(matrix[1, 0], matrix[0, 0]))