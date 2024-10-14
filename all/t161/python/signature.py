from typing import Dict, List


def generate_combinations(map: Dict[str, List[int]]) -> List[List[int]]:
    """
    Produces all combinations of numeric arrays for each key in the given map object and returns them as a two-dimensional array.

    Args:
        map (Dict[str, List[int]]): A map where each key is a string, and each value is an array of numbers.

    Returns:
        List[List[int]]: An array of arrays, where each sub-array is a unique combination of numbers from the map's values.
    """