import re

def parse_markdown_titles(markdown: str) -> Dict[str, List[str]]:
    h1_titles = re.findall(r'^# (.*)', markdown, re.MULTILINE)
    h2_titles = re.findall(r'^## (.*)', markdown, re.MULTILINE)
    h3_titles = re.findall(r'^### (.*)', markdown, re.MULTILINE)

    return {
        'level1': h1_titles,
        'level2': h2_titles,
        'level3': h3_titles,
    }
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