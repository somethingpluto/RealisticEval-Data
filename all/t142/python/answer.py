import re

def camel_case_to_capitalized_with_spaces(input: str) -> str:
    # Use a regular expression to insert spaces before capital letters and numbers
    spaced_string = re.sub(r'([A-Z0-9])', r' \1', input)

    # Capitalize the first letter of each word
    capitalized_string = ' '.join(word.capitalize() for word in spaced_string.split())

    # Trim any leading spaces and return the result
    return capitalized_string.strip()
