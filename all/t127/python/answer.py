from typing import List, Dict, Any


def separate_octave_and_root(midi_notes: List[int]) -> Dict[str, List[int]]:
    """
    Splits a list of MIDI note numbers into separate lists of octaves and root notes.

    Args:
        midi_notes (List[int]): An array of MIDI note numbers.

    Returns:
        Dict[str, List[int]]: A dictionary containing lists of octaves and root notes.

    Raises:
        TypeError: If the input is not a list of integers.
    """
    if not isinstance(midi_notes, list) or not all(isinstance(note, int) for note in midi_notes):
        raise TypeError('Input must be an array of integers.')

    octave_notes = []
    root_notes = []

    for note in midi_notes:
        octave = note // 12  # Calculate the octave by integer division
        root_note = note % 12  # Calculate the root note as the remainder
        octave_notes.append(octave)
        root_notes.append(root_note)

    return {
        'octaveNotes': octave_notes,
        'rootNotes': root_notes
    }