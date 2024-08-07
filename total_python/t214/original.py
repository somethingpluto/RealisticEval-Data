#
# Read the mapping file and creates a dictionary where the keys are the old words 
# and the values are the new words. The old word and new word must be enclosed in
# single quotes and separated by a comma. The first token (the old word) can be 
# a regular expression. Leading and trailing spaces are preserved within the 
# single-quoted strings and regular expressions.
#
def read_mapping_file(mapping_file_path):
    """Read the mapping file and return a list of tuples with compiled regex and replacement strings."""
    mappings = []
    with open(mapping_file_path, 'r') as mapping_file:
        for line in mapping_file:
            old_pattern, _, new_word = line.partition(',')
            old_pattern = old_pattern.strip().strip("'")  # Remove leading/trailing spaces and quotes
            new_word = new_word.strip().strip("'")  # Remove leading/trailing spaces and quotes
            mappings.append((re.compile(old_pattern), new_word))
    return mappings
