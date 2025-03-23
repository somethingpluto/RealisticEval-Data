

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)

from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    min_val = min(numbers)
    second_min_val = min(numbers[i] for i in range(1, len(numbers)) if numbers[i]!= min_val)
    closest_pair = (min_val, second_min_val)

    for number in numbers:
        if abs(number - min_val) < abs(second_min_val - min_val):
            second_min_val = number
            if number!= min_val:
                closest_pair = (min_val, second_min_val)

    return closest_pair
candidate = find_closest_elements
check(candidate)