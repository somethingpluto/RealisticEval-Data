from typing import Dict


def check_sequences(filename:str) -> Dict:
    """
    Read multiple sequences from the file and determine if each sequence is a "Munodi sequence". The definition of the Munodi sequence is based on a specific recursive relationship, that is, for even numbers, the next term is half of it, for odd numbers, the next term is 3*n + 1, and the sequence terminates when it encounters 1.
    For example: (2, 4, 6, 8) is Mundi sequence

    Args:
        filename(str): file path

    Returns:
        Dict: sequences weather is Munodi sequence
    """