import re


def clean_pattern(x, pattern):
    """
    Extracts a numeric value from the input string based on the given regex pattern.

    Args:
        x (str or any): The input from which to extract the value. It will be converted to a string.
        pattern (str): The regular expression pattern to use for matching.

    Returns:
        float: The extracted weight value if a match is found, otherwise an empty string.
    """
    # Convert input to string
    x = str(x)

    # Search for the pattern in the input string
    match = re.search(pattern, x)

    if match:
        # Extract the weight value from the first matching group
        weight = match.group(1)  # Can also use match.group(3) if needed
        try:
            # Convert the weight to a float and return it
            weight_value = float(weight)
            return weight_value
        except ValueError:
            # Handle cases where conversion to float fails
            print(f"Warning: Unable to convert '{weight}' to float.")
            return ''
    else:
        return ''  # Return empty string if no match is found
