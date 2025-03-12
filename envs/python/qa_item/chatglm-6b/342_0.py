
from typing import Dict, List

def parse_markdown_titles(markdown: str) -> Dict[str, List[str]]:
    """
    Parses markdown text to extract titles of different levels.

    This function takes a string of markdown content as input and returns an
    object containing arrays of titles categorized by their level:
    level 1 (H1), level 2 (H2), and level 3 (H3).

    Args:
        markdown (str): A string containing markdown formatted text.

    Returns:
        Dict[str, List[str]]: A dictionary with three properties: level1, level2, and level3,
                               each holding a list of corresponding titles found in the markdown.
    """
    # Validate markdown input
    if not markdown:
        raise ValueError("Invalid markdown input")

    # Split markdown into title and body text
    titles = markdown.split(" ")

    # Create dictionary with H1, H2, and H3 titles
    level_dict = {}
    for title in titles:
        if title.lower() in ["h1", "h2", "h3"]:
            level_dict[title.lower()] = []
        else:
            level_dict[title.lower()] = [title]

    # Return dictionary with level1, level2, and level3 titles
    return level_dict

import unittest


class TestParseMarkdownTitles(unittest.TestCase):

    def test_extract_first_second_and_third_level_titles(self):
        markdown = """        
        # Title 1
        Content here.
        ## Subtitle 1.1
        More content.
        ### Subsubtitle 1.1.1
        Even more content.
        # Title 2
        Another content.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1", "Title 2"],
            'level2': ["Subtitle 1.1"],
            'level3': ["Subsubtitle 1.1.1"],
        })

    def test_handle_missing_headers(self):
        markdown = """        
        This is just some text without headers.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': [],
            'level2': [],
            'level3': [],
        })

    def test_handle_only_first_level_headers(self):
        markdown = """        
        # Only Title 1
        Content without subtitles.

        # Only Title 2
        More content.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Only Title 1", "Only Title 2"],
            'level2': [],
            'level3': [],
        })

    def test_handle_mixed_headers_with_empty_lines(self):
        markdown = """        
        # Title 1
        ## Subtitle 1.1
        Some content here.
        ### Subsubtitle 1.1.1

        # Title 2
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1", "Title 2"],
            'level2': ["Subtitle 1.1"],
            'level3': ["Subsubtitle 1.1.1"],
        })

    def test_handle_headers_with_special_characters(self):
        markdown = """        
        # Title 1 - Special Characters!
        ## Subtitle 1.1: The Beginning
        ### Subsubtitle 1.1.1 (Note)
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1 - Special Characters!"],
            'level2': ["Subtitle 1.1: The Beginning"],
            'level3': ["Subsubtitle 1.1.1 (Note)"],
        })

if __name__ == '__main__':
    unittest.main()