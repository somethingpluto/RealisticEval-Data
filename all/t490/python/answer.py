def format_str(x:str):
    # Convert x to string if it's not already a string
    if not isinstance(x, str):
        x = str(x)

    # Ensure there is a matching number of code block delimiters
    if x.count("```") % 2 == 1:
        x += "\n```"

    # Format each line by prepending '> ' and join them with newlines
    formatted_lines = ["> " + line for line in x.split("\n")]
    return "\n".join(formatted_lines)
