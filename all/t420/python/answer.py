def read_file_as_sequences(file_path):
    """Read the file and convert each line into a list of words."""
    with open(file_path, 'r') as file:
        return [line.strip().split() for line in file]


def find_closest_word_indices(sequence, word1, word2):
    """Find the indices of two words in a sequence and calculate their closest distances."""
    word1_indices = []
    word2_indices = []
    min_distance = float('inf')

    # Gather indices for both words
    for index, word in enumerate(sequence):
        if word == word1:
            word1_indices.append(index)
        elif word == word2:
            word2_indices.append(index)

    # Calculate the minimum distance between all pairs of indices
    for index1 in word1_indices:
        for index2 in word2_indices:
            distance = abs(index1 - index2)
            if distance < min_distance:
                min_distance = distance

    return min_distance


def get_min_distance_between_2_word(file_path, word1, word2):
    """Determine the minimum distance between two words in any line of a file."""
    sequences = read_file_as_sequences(file_path)
    min_distance = float('inf')
    min_seq_num = None

    for i, seq in enumerate(sequences):
        distance = find_closest_word_indices(seq, word1, word2)
        if distance < min_distance:
            min_distance = distance
            min_seq_num = i

    return min_seq_num, min_distance if min_distance != float('inf') else (None, None)
