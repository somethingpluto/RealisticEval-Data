def trapezoidal_rule(func, a: float, b: float, n: int) -> float:
    """
    Calculate the integral approximation of a given function on the interval [a, b] using the trapezoidal rule.

    Args:
        func (callable): The function to integrate, which takes a float and returns a float.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of subintervals to use in the approximation (more intervals yield higher accuracy).

    Returns:
        float: The approximate value of the integral over the interval [a, b].
    """