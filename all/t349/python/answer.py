from typing import List, Any


def generate_combinations(input_lists: List[List[Any]]) -> List[List[Any]]:
    if input_lists is None or len(input_lists) == 0:
        return []  # Return an empty list if input is None or empty
    combinations = []
    _generate_combinations_recursive(input_lists, 0, [], combinations)
    return combinations


def _generate_combinations_recursive(input_lists: List[List[Any]], current_index: int,
                                     current_combination: List[Any], combinations: List[List[Any]]):
    if current_index == len(input_lists):
        combinations.append(current_combination.copy())  # Snapshot of current_combination
        return
    current_list = input_lists[current_index]
    for element in current_list:
        current_combination.append(element)
        _generate_combinations_recursive(input_lists, current_index + 1, current_combination, combinations)
        current_combination.pop()  # Remove the last element for backtracking
