import re


def extract_code_blocks(markdown):
    """
    Extracts the contents of code blocks from the given Markdown string.

    Args:
    markdown (str): The Markdown text containing code blocks.

    Returns:
    list of str: A list containing the contents of each code block found.
    """
    # Regex to find code blocks enclosed in triple backticks
    pattern = r"```[\s\S]+?```"
    matches = re.findall(pattern, markdown)
    extracted_content = []

    for match in matches:
        # Remove the surrounding backticks and potential language specification
        cleaned = re.sub(r'^```.*?\n', '', match)  # Remove starting backticks with language
        cleaned = re.sub(r'```$', '', cleaned)  # Remove ending backticks
        extracted_content.append(cleaned.strip())

    return extracted_content