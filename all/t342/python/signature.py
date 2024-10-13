def parse_markdown_titles(markdown: str) -> dict[str, list[str]]:
    """
    Parses markdown text to extract titles of different levels.

    This function takes a string of markdown content as input and returns an
    object containing arrays of titles categorized by their level:
    level 1 (H1), level 2 (H2), and level 3 (H3).

    Args:
        markdown (str): A string containing markdown formatted text.

    Returns:
        dict[str, list[str]]: A dictionary with three properties: level1, level2, and level3,
                               each holding a list of corresponding titles found in the markdown.
    """
