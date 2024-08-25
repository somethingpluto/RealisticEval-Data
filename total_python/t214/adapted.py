import re


def read_mapping_file(mapping_file_path):
    """
    Read a mapping file and return a list of tuples with compiled regex and replacement strings.

    Args:
    mapping_file_path (str): Path to the file containing regex mappings.

    Returns:
    list of tuples: Each tuple contains a compiled regex object and a corresponding replacement string.

    Raises:
    FileNotFoundError: If the mapping file does not exist.
    ValueError: If any line in the file does not contain exactly one comma.

    Example of file format:
    'old_pattern1','new_word1'
    'old_pattern2','new_word2'
    """
    mappings = []
    try:
        with open(mapping_file_path, 'r') as mapping_file:
            for line in mapping_file:
                if ',' not in line:
                    raise ValueError(
                        "Each line must contain exactly one comma separating the pattern and the replacement.")

                old_pattern, new_word = line.strip().split(',', 1)
                old_pattern = old_pattern.strip().strip("'")  # Remove leading/trailing spaces and single quotes
                new_word = new_word.strip().strip("'")  # Remove leading/trailing spaces and single quotes
                mappings.append((re.compile(old_pattern), new_word))
    except FileNotFoundError:
        raise FileNotFoundError(f"Unable to find the specified file: {mapping_file_path}")

    return mappings