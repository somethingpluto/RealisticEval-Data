def convert_to_ring_format(holes):
    """Convert a list of hole positions to the ring format (list of 1s and 0s)."""
    ring = [1] * 32
    for hole in holes:
        ring[hole] = 0
    return ring