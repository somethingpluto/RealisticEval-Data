from music21 import pitch


def adjust_to_c_major(note_name):
    """
    Adjusts a given musical note to the nearest note in the C major scale.

    Args:
        note_name (str): The name of the note to adjust.

    Returns:
        str: The adjusted note name with octave if applicable, or the input note if already in C major.
    """
    c_major_scale = ["C", "D", "E", "F", "G", "A", "B"]

    # Attempt to create a Pitch object from the note_name
    try:
        given_pitch = pitch.Pitch(note_name)
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
        if neighbor_pitch.name in c_major_scale:
            return neighbor_pitch.nameWithOctave

    # If no close C major note is found, return the original note (this is a fallback, should not generally happen)
    return note_name
