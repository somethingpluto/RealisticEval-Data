from typing import List


def min_removals_to_make_unique(nums: List[int]) -> int:
    numbers = []
    minimum_distinct = 0
    for number in nums:
        if number in numbers:
            minimum_distinct += 1
            numbers.remove(number)
        numbers.append(number)
    return minimum_distinct