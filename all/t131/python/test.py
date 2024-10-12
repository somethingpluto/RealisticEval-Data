class TestCSSHighlightAdd(unittest.TestCase):
    def setUp(self):
        # Create a mock document for testing
        self.document = MockDocument()
        self.css_rule_exists_for_highlight = False
        self.style_element = '<style></style>'
        self.document.head.append_child(self.style_element)

    def check_css_highlight_and_add(self):
        if not self.css_rule_exists_for_highlight:
            # Create a new CSS rule
            css_rule = ".highlight { background-color: yellow; color: black; }"
            self.document.style_sheets[0].insert_rule(css_rule, 0)
            self.css_rule_exists_for_highlight = True

    def test_add_style_element_with_highlight_css_rule(self):
        self.check_css_highlight_and_add()
        # Check that the style element contains the correct CSS rule
        self.assertIn("background-color: yellow;", self.document.style_sheets[0].css_rules[0])

    def test_do_not_add_new_css_rule_if_exists(self):
        # Manually add the rule to simulate existing condition
        self.document.style_sheets[0].insert_rule(".highlight { background-color: yellow; }", 0)
        self.check_css_highlight_and_add()
        # Check that only one rule is present
        self.assertEqual(len(self.document.style_sheets[0].css_rules), 1)

    def test_add_only_one_rule_even_if_called_multiple_times(self):
        self.check_css_highlight_and_add()
        self.check_css_highlight_and_add()  # Call the function again
        # Check that only one rule is present
        self.assertEqual(len(self.document.style_sheets[0].css_rules), 1)

    def test_correctly_append_style_element_to_head(self):
        self.check_css_highlight_and_add()
        # Check that the style element is indeed appended to the head
        self.assertTrue(self.document.head.contains(self.style_element))

