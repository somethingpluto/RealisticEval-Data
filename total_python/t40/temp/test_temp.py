import unittest


class TestAdjustToCMajor(unittest.TestCase):
    def test_note_already_in_c_major(self):
        self.assertEqual(adjust_to_c_major("C4"), "C4")
        self.assertEqual(adjust_to_c_major("G3"), "G3")

    def test_note_not_in_c_major(self):
        self.assertEqual(adjust_to_c_major("C#4"), "D4")
        self.assertEqual(adjust_to_c_major("F#3"), "G3")

    def test_invalid_note_name(self):
        self.assertEqual(adjust_to_c_major("H2"), "C4")

from music21 import pitch


def adjust_to_c_major(note_name):
    c_major_scale = ["C", "D", "E", "F", "G", "A", "B"]

    # Attempt to create a Pitch object from the note_name
    try:
        given_pitch = pitch.Pitch(note_name)
        print(f"Created pitch: {given_pitch.nameWithOctave}")  # Debug: show created pitch
    except Exception as e:
        print(f"Error: {e}. Invalid note name provided. Returning 'C4' as a default.")
        return "C4"

    # If the note is already in the C major scale, return it as is
    if given_pitch.name in c_major_scale:
        return given_pitch.nameWithOctave

    # Attempt to find the closest note in the C major scale, either up or down
    search_directions = [1, -1]  # Represents semitone adjustments: up 1 and down 1
    for direction in search_directions:
        neighbor_pitch = given_pitch.transpose(direction)
        print(f"Checking neighbor pitch: {neighbor_pitch.nameWithOctave}")  # Debug: show neighbor pitch
        if neighbor_pitch.name in c_major_scale:
            return neighbor_pitch.nameWithOctave

    # If no close C major note is found, return the original note (this is a fallback, should not generally happen)
    return note_name
