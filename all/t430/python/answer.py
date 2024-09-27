def intersect_vertically(rect1, rect2):
    """
    Determine if two rectangles intersect vertically.

    Each rectangle is defined by a tuple (x1, y1, x2, y2), where:
    - (x1, y1) are the coordinates of the bottom-left corner.
    - (x2, y2) are the coordinates of the top-right corner.

    Args:
        rect1 (tuple): The first rectangle defined by (x1, y1, x2, y2).
        rect2 (tuple): The second rectangle defined by (x1, y1, x2, y2).

    Returns:
        bool: True if the rectangles intersect vertically, False otherwise.
    """
    return not (rect1[3] < rect2[1] or rect2[3] < rect1[1])