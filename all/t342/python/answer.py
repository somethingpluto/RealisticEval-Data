def parse_markdown_titles(markdown: str) -> dict:
    """
    Parses markdown text to extract titles of different levels.

    This function takes a string of markdown content as input and returns an
    object containing arrays of titles categorized by their level:
    level 1 (H1), level 2 (H2), and level 3 (H3).

    Args:
        markdown (str): A string containing markdown formatted text.

    Returns:
        dict: An object with three properties: level1, level2, and level3,
              each holding an array of corresponding titles found in the markdown.
    """
    # Initialize a dictionary to store titles categorized by their levels.
    result = {
        'level1': [],  # List to store level 1 titles (H1)
        'level2': [],  # List to store level 2 titles (H2)
        'level3': []  # List to store level 3 titles (H3)
    }

    # Split the input markdown text into individual lines.
    lines = markdown.split('\n')

    # Iterate through each line in the markdown content.
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace from the line.

        # Check if the line starts with a level 1 markdown header (#).
        if line.startswith('# '):
            # Extract the title after the header and push it to level1 list.
            result['level1'].append(line[2:])  # Remove the '# ' prefix.

        # Check if the line starts with a level 2 markdown header (##).
        elif line.startswith('## '):
            # Extract the title after the header and push it to level2 list.
            result['level2'].append(line[3:])  # Remove the '## ' prefix.

        # Check if the line starts with a level 3 markdown header (###).
        elif line.startswith('### '):
            # Extract the title after the header and push it to level3 list.
            result['level3'].append(line[4:])  # Remove the '### ' prefix.

    # Return the dictionary containing categorized titles.
    return result