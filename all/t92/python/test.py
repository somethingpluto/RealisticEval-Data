class TestReplaceHtmlEntities(unittest.TestCase):

    def test_decodes_standard_html_entities(self):
        input_string = 'The &amp; symbol should become an &quot;and&quot; sign.'
        expected = 'The & symbol should become an "and" sign.'
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_returns_empty_string_for_empty_input(self):
        input_string = ''
        expected = ''
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_decodes_multiple_different_entities_in_one_string(self):
        input_string = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;'
        expected = '<div>Hello & Welcome to the \'World\'!</div>'
        self.assertEqual(replace_html_entities(input_string), expected)

    def test_handles_strings_with_no_entities(self):
        input_string = 'Just a normal string without entities.'
        expected = 'Just a normal string without entities.'
        self.assertEqual(replace_html_entities(input_string), expected)
