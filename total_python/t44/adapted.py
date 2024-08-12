def string_side_by_side(string1, string2, column_width=20):
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    max_length = max(len(lines1), len(lines2))
    lines1 += [''] * (max_length - len(lines1))
    lines2 += [''] * (max_length - len(lines2))

    formatted_lines = (f"{line1:<{column_width}} | {line2:<{column_width}}"
                       for line1, line2 in zip(lines1, lines2))

    return '\n'.join(formatted_lines)
