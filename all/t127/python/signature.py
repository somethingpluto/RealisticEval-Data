from typing import List


def separate_octave_and_root(midi_notes: List[int])->dict:
    """
    Splits a list of MIDI note numbers into separate lists of octaves and root notes.

    Args:
        midi_notes (List[int]): A list of MIDI note numbers.

    Returns:
        dict: A dictionary containing lists of octaves and root notes.
    """
