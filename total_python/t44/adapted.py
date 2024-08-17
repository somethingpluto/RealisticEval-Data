def string_side_by_side(string1, string2, column_width=20):
    # Split the strings into lists of lines
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    # Find the maximum length of the two lists
    max_length = max(len(lines1), len(lines2))

    # Pad both lists to have the same number of lines
    padded_lines1 = [line.ljust(column_width) for line in lines1] + [' ' * column_width] * (max_length - len(lines1))
    padded_lines2 = [line.ljust(column_width) for line in lines2] + [' ' * column_width] * (max_length - len(lines2))

    # Use a list comprehension to format and concatenate lines
    formatted_lines = [f"{line1} | {line2}" for line1, line2 in zip(padded_lines1, padded_lines2)]

    # Join all formatted lines into a single string
    return '\n'.join(formatted_lines)
