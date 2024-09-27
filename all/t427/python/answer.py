def read_sequences_from_file(filename):
    """Read sequences from a file and return them as a list of lists."""
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            # Assuming sequences are comma-separated in the file
            seq = list(map(int, line.strip().split(',')))  # Convert to a list of integers
            sequences.append(seq)
    return sequences


def is_munodi_sequence(sequence):
    """Check if the given sequence is a Munodi sequence."""
    if len(sequence) < 2:
        return False  # A sequence with less than 2 elements cannot be a Munodi sequence

    common_difference = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != common_difference:
            return False  # Found a different difference, not a Munodi sequence
    return True  # All differences are the same


def check_sequences(filename):
    """Read sequences from a file and determine if each is a Munodi sequence."""
    sequences = read_sequences_from_file(filename)
    results = {}
    for seq in sequences:
        results[tuple(seq)] = is_munodi_sequence(seq)
    return results
