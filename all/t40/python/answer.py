def adjust_to_c_major(note):
    # Strip spaces and convert to upper case
    base_note = note.strip().upper()

    # Normalization dictionary for flats and sharps
    note_normalization = {
        'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'
    }

    # Convert flats to sharps
    if base_note in note_normalization:
        base_note = note_normalization[base_note]

    # C Major scale notes (without sharps and flats)
    c_major_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    # Chromatic scale including sharps
    chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_index = chromatic_scale.index(base_note)

    # Find the nearest C Major note
    min_distance = float('inf')
    closest_note = None
    for scale_note in c_major_scale:
        scale_index = chromatic_scale.index(scale_note)
        # Calculate minimal circular distance
        distance = min(abs(scale_index - note_index), 12 - abs(scale_index - note_index))
        if distance < min_distance:
            min_distance = distance
            closest_note = scale_note

    return closest_note
