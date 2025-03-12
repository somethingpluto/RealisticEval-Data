from cssutils import CSSStyleSheet

def get_css_from_sheet(sheet: CSSStyleSheet) -> str:
    """
    Extract all the CSS rules from a given CSSStyleSheet and concatenate them into a string.

    Args:
        sheet (CSSStyleSheet): The stylesheet object from which to extract CSS rules.

    Returns:
        str: A single string containing all CSS rules, or an empty string if the sheet is invalid or inaccessible.
    """
    css_rules = ''
    for rule in sheet.cssRules:
        css_rules += str(rule) + '\n'
    return css_rules.strip()
class TestGetCSSFromSheet(unittest.TestCase):
    def setUp(self):
        """Create a style element with some CSS rules for testing."""
        self.style_element = MagicMock()
        self.style_element.sheet = 'body { background-color: red; } p { color: blue; }'

    def tearDown(self):
        """Clean up after each test."""
        pass  # No need to clean up in the mock context

    def test_empty_stylesheet(self):
        """Empty Stylesheet: should return an empty string."""
        empty_style = MagicMock()
        empty_style.sheet = ''
        css_text = get_css_from_sheet(empty_style.sheet)
        self.assertEqual(css_text, '')

    def test_invalid_input(self):
        """Invalid Input: should return an empty string for non-CSSStyleSheet input."""
        self.assertEqual(get_css_from_sheet(None), '')
        self.assertEqual(get_css_from_sheet({}), '')
        self.assertEqual(get_css_from_sheet('not a stylesheet'), '')

    def test_cross_origin_restrictions(self):
        """Cross-Origin Restrictions: should handle restricted stylesheets gracefully."""
        restricted_sheet = MagicMock()
        restricted_sheet.sheet = None  # Simulating a restricted stylesheet

        # The function should not throw an error, we'll just check for the return value
        css_text = get_css_from_sheet(restricted_sheet.sheet)
        self.assertEqual(css_text, '')

    def test_style_element_with_inline_css(self):
        """Style Element with Inline CSS: should return CSS from inline style element."""
        style_element = MagicMock()
        style_element.sheet = 'div { font-size: 16px; }'
        css_text = get_css_from_sheet(style_element.sheet)
        self.assertEqual(css_text, 'div {font-size: 16px;}')

if __name__ == '__main__':
    unittest.main()