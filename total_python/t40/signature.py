from music21 import pitch


def adjust_to_c_major(note_name: str) -> str:
    """
    Adjusts a given musical note to the nearest note in the C major scale.
    Args:
        note_name (str): The name of the note to adjust.

    Returns:
        str: The adjusted note name with octave if applicable, or the input note if already in C major.
    """
