def josephus(n: int, k: int) -> int:
    """
    Simulates the Josephus problem using a list to represent the circle of people.
    Args:
        n (int): The number of people in the circle (1 to n).
        k (int): The step count (every k-th person will be eliminated).

    Returns:
        int: The position of the last person remaining (1-indexed).
    """
