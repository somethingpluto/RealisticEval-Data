def create_circle_of_fifths(starting_note: str) -> list[str]:
    """
    Generates a cyclic tone sequence of five degrees of length 12 starting with the specified starting note.

    Args:
        starting_note (str): The musical note to start the Circle of Fifths from (e.g., "C").

    Returns:
        list[str]: A list representing the Circle of Fifths.
    """

    # Define the perfect fifth intervals in terms of note names
    fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']

    # Create a mapping of note names to indices for easier manipulation
    note_index = {note: i for i, note in enumerate(fifths)}

    # Start with the given note
    if starting_note not in note_index:
        raise ValueError(f"Invalid starting note: {starting_note}")

    current_index = note_index[starting_note]
    circle = [starting_note]  # Start the circle with the initial note

    # Generate the next 11 notes in the Circle of Fifths
    for _ in range(11):
        current_index = (current_index + 1) % len(fifths)  # Move to the next index (perfect fifth)
        circle.append(fifths[current_index])  # Add the transposed note to the circle

    return circle  # Return the full Circle of Fifths

