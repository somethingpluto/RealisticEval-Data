import numpy as np


def get_mids_from_edges(edges: np.ndarray):
    """
    Calculate the midpoints from a given array of edges.
    For example:
        input: [0, 1, 2]
        output: [0.5, 1.5]

    Args:
        edges (np.ndarray): An array of edge values.

    Returns:
        np.ndarray: An array of midpoints calculated from the edges.
    """
