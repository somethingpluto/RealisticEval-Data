from typing import List, Dict


def generate_combinations(map: Dict[str, List[int]]) -> List[List[int]]:
    """
    Produces all combinations of numeric arrays for each key in the given map object
    and returns them as a two-dimensional array.

    Args:
        map (Dict[str, List[int]]): A map where each key is a string, and each value is an array of numbers.

    Returns:
        List[List[int]]: An array of arrays, where each sub-array is a unique combination
                          of numbers from the map's values.
    """
    keys = list(map.keys())
    values = list(map.values())
    combinations = []

    def generate(current_combination: List[int], current_index: int) -> None:
        """
        Helper function to recursively generate combinations.

        Args:
            current_combination (List[int]): The current combination being built.
            current_index (int): The current index in the keys/values arrays.
        """
        # Base case: If we've reached the end of the keys, push the combination to the result.
        if current_index == len(keys):
            combinations.append(current_combination.copy())
            return

        # Recursively generate combinations for the current key's values.
        current_values = values[current_index]
        for value in current_values:
            current_combination.append(value)
            generate(current_combination, current_index + 1)
            current_combination.pop()  # backtrack to try the next value

    # Start the recursive combination generation.
    generate([], 0)
    return combinations