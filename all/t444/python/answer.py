def format_comment(string, max_length=60):
    """
    Formats a string into a commented block with specified maximum line length.

    Args:
        string (str): The input string to format.
        max_length (int): Maximum length of each line in the output.

    Returns:
        str: A formatted string with each line prefixed by '# ' and not exceeding the specified max_length.
    """
    # Split the string into lines
    lines = string.split('\n')

    # Initialize a list to store the formatted lines
    formatted_lines = []

    # Iterate through the lines
    for line in lines:
        # Split the line into words
        words = line.split()

        # Initialize a variable to keep track of the current line
        current_line = ''

        # Iterate through the words
        for word in words:
            # If adding the next word exceeds max length, append the current line to formatted lines
            if len(current_line) + len(word) + 1 > max_length:
                formatted_lines.append(current_line)
                current_line = word  # Start a new line with the current word
            else:
                # Append the word to the current line
                current_line = current_line + ' ' + word if current_line else word

        # Append any remaining text in the current line to the formatted lines
        if current_line:
            formatted_lines.append(current_line)

    # Prefix each line with '# ' and join them into a single string
    return '\n'.join(['# ' + line for line in formatted_lines])
