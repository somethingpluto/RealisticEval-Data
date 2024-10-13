def reverse_range(v: list[int], a: int, b: int) -> None:
    """
    Reverses a range of elements in the list v from index a to index b (inclusive).

    Args:
        v (list[int]): The list of integers to modify.
        a (int): The starting index of the range to reverse.
        b (int): The ending index of the range to reverse.

    Raises:
        ValueError: If the indices are invalid.
    """
    if a < 0 or b >= len(v) or a > b:
        print("Invalid indices")
        return

    # Reverse the sublist from index a to b (inclusive)
    v[a:b + 1] = reversed(v[a:b + 1])
