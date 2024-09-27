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
            # If the current line plus the next word would be too long,
            # append the current line to the list of formatted lines and start a new line
            if len(current_line) + len(word) > max_length:
                formatted_lines.append(current_line)
                current_line = ''

            # If the current line is empty, add the word to the line
            # Otherwise, add a space and the word to the line
            if current_line == '':
                current_line = word
            else:
                current_line += ' ' + word

        # Add the remaining line to the list of formatted lines
        formatted_lines.append(current_line)

    # Return the formatted comment
    return '\n'.join(['# ' + line for line in formatted_lines])
