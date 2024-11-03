def extract_string_from_braces(input_string):
    # Find the position of the first opening brace
    opening_brace_pos = input_string.find('{')

    # Check if an opening brace was found
    if opening_brace_pos == -1:
        return "No opening brace found."

    # Find the position of the first closing brace after the opening brace
    closing_brace_pos = input_string.find('}', opening_brace_pos)

    # Check if a closing brace was found
    if closing_brace_pos == -1:
        return "No closing brace found."

    # Extract the string between the braces (including the braces)
    return input_string[opening_brace_pos:closing_brace_pos + 1]