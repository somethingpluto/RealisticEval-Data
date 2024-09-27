from typing import List


def get_max_people(people: List[int], status: List[str]) -> int:
    """
    Amazon is organizing a farewell party for its interns at a large party hall! There are q events in the form "+x" and "-x" that denote person x has entered or left the party, respectively.   Find the maximum number of people at any time at the party.Return -1 if the series of events is not possible.

    Args:
        people(List[int]): people array
        status(List[str]): people action array

    Returns:
        int: the maximum number of people at any time at the party or -1 is series of events is not possible
    """
