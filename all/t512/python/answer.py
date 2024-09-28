def convert_to_ring_format(holes):
    """
    Convert a list of hole positions to the ring format (list of 1s and 0s).

    Parameters:
    holes (list): A list of integers representing the positions of the holes (0-indexed).

    Returns:
    list: A list of length 32, where positions with holes are 0 and others are 1.
    """
    # Initialize the ring with all positions set to 1
    ring = [1] * 32

    # Mark the positions of holes as 0
    for hole in holes:
        if 0 <= hole < 32:  # Ensure hole positions are within valid range
            ring[hole] = 0

    return ring
