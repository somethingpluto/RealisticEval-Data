import numpy as np


def get_mids_from_edges(edges):
    """
    Calculate the midpoints from a given array of edges.

    Args:
        edges (np.ndarray): An array of edge values.

    Returns:
        np.ndarray: An array of midpoints calculated from the edges.
    """
    # Ensure edges is a numpy array for consistency
    edges = np.asarray(edges)

    # Calculate midpoints using vectorized operations
    mids = (edges[:-1] + edges[1:]) / 2

    return mids