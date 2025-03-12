from typing import List

def separate_octave_and_root(midi_notes: List[int])->dict:
    """
    Splits a list of MIDI note numbers into separate lists of octaves and root notes.

    Args:
        midi_notes (List[int]): A list of MIDI note numbers.

    Returns:
        dict: A dictionary containing lists of octaves and root notes.
    """
    octaves = []
    root_notes = []
    
    for note in midi_notes:
        octave = note // 12
        root_note = note % 12
        octaves.append(octave)
        root_notes.append(root_note)
    
    return {'octaves': octaves, 'root_notes': root_notes}
import unittest


class TestSeparateOctaveAndRoot(unittest.TestCase):

    def test_correctly_separates_midi_notes(self):
        midi_notes = [60, 61, 62]  # C4, C#4, D4
        expected = {
            'octaveNotes': [5, 5, 5],  # All notes are in the 5th octave
            'rootNotes': [0, 1, 2]     # Root notes are C, C#, D
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_handles_single_midi_note_input(self):
        midi_notes = [24]  # C1
        expected = {
            'octaveNotes': [2],  # 2nd octave
            'rootNotes': [0]     # C note
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_returns_empty_arrays_for_empty_input_array(self):
        midi_notes = []
        expected = {
            'octaveNotes': [],
            'rootNotes': []
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_throws_error_for_invalid_input_types(self):
        invalid_inputs = ["not an array", [3.14]]
        for invalid_input in invalid_inputs:
            with self.assertRaises(TypeError):
                separate_octave_and_root(invalid_input)

    def test_handles_midi_notes_from_different_octaves(self):
        midi_notes = [12, 25, 37]  # C1, C#2, D#3
        expected = {
            'octaveNotes': [1, 2, 3],  # 1st, 2nd, and 3rd octaves
            'rootNotes': [0, 1, 1]     # Root notes are C, C#, D#
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

if __name__ == '__main__':
    unittest.main()