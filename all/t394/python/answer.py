import numpy as np


def gradient_descent_euclidean(start, learning_rate, n_steps, grad_f):
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
    x = np.array(start)  # Ensure start is a numpy array
    path = [x.copy()]  # Store the initial point

    for _ in range(n_steps):
        gradient = grad_f(x)  # Calculate the gradient at the current point
        x = x - learning_rate * gradient  # Update the current point
        path.append(x.copy())  # Store the new point

    return np.array(path)  # Convert the path list to a numpy array for return
