import re

def split_by_html_tags(input_string: str) -> list[str]:
    """
    Splits the input string by specific HTML tags (<p>, <ul>, <ol>)
    and returns a list containing the split results without HTML tags.

    Args:
        input_string (str): The input string containing HTML tags.

    Returns:
        list[str]: A list of strings split by the specified HTML tags.
    """
    # Regular expression pattern to match <p>, <ul>, and <ol> tags
    pattern = re.compile(r"<p>(.*?)</p>|<ul>(.*?)</ul>|<ol>(.*?)</ol>", re.DOTALL)

    # Find all matches
    matches = pattern.findall(input_string)

    # Prepare results list
    result = []

    # Append content without HTML tags to the results list
    for match in matches:
        for content in match:
            if content.strip():  # Only add non-empty content
                result.append(content.strip())

    # Add any non-matching parts (text outside tags)
    parts = some_split_logic(input_string)  # Replace with your actual split logic
    for part in parts:
        if part.strip() and not any(tag in part for tag in ['<p>', '<ul>', '<ol>']):
            result.append(part.strip())

    return result