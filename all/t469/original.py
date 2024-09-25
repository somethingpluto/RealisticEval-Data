
def get_scale(matrix: 'rai.typing.Affine') -> tuple[np.float64, np.float64]:
    """
    Given an affine matrix, return the corresponding scale.
    Written by ChatGPT
    """
    scale_x = np.linalg.norm(matrix[:, 0])
    scale_y = np.linalg.norm(matrix[:, 1])
    return scale_x, scale_y