from typing import List, Tuple

def extract_name_and_number(s: str) -> Tuple[str, int]:
    """
    Extracts the name and number from a string in the format "name + number".

    This helper function splits the input string into its name and number components.
    It assumes that the string is well-formed, with the name part consisting of alphabetic characters
    and the number part consisting of numeric digits.

    :param s: The input string in the format "name + number".
    :return: A tuple containing the name as a string and the number as an integer.
    """
    pos = len(s) - 1
    while pos >= 0 and s[pos].isdigit():
        pos -= 1
    name = s[:pos + 1].strip()  # Get name and remove any leading/trailing spaces
    number = int(s[pos + 1:].strip())  # Get the number and convert it to an integer
    return name, number

def sort_names(arr: List[str]) -> List[str]:
    """
    Sort the list of strings with the format "name + number" in ascending order.
    If the numbers are the same, sort by name in ascending order.

    :param arr: A list of strings to be sorted.
    :return: A list of strings sorted according to the rules described above.
    """
    sorted_arr = sorted(arr, key=lambda x: (extract_name_and_number(x)[1], extract_name_and_number(x)[0]))
    return sorted_arr
