from typing import Callable

import numpy as np


def gradient_descent_euclidean(start: np.array, learning_rate: float, n_steps: int, grad_f: Callable):
    """
    Performs gradient descent to minimize a function.

    Args:
        start (np.ndarray): The starting point for the gradient descent.
        learning_rate (float): The learning rate for the updates.
        n_steps (int): The number of steps to perform in the gradient descent.
        grad_f (callable): A function that computes the gradient of the objective function.

    Returns:
        np.ndarray: The path taken during the gradient descent.
    """
