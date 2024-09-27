import unittest

class TestSplitByHtmlTags(unittest.TestCase):

    def test_single_paragraph(self):
        input_string = "<p>This is a paragraph.</p>"
        expected_output = ["This is a paragraph."]
        self.assertEqual(split_by_html_tags(input_string), expected_output)

    def test_multiple_paragraphs(self):
        input_string = "<p>First paragraph.</p><p>Second paragraph.</p>"
        expected_output = ["First paragraph.", "Second paragraph."]
        self.assertEqual(split_by_html_tags(input_string), expected_output)

    def test_list_tags(self):
        input_string = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        expected_output = []
        self.assertEqual(split_by_html_tags(input_string), expected_output)

    def test_mixed_tags(self):
        input_string = (
            "<p>Paragraph 1.</p>"
            "<ul><li>List Item 1</li><li>List Item 2</li></ul>"
            "<p>Paragraph 2.</p>"
            "<ol><li>Ordered Item 1</li></ol>"
        )
        expected_output = [
            "Paragraph 1.",
            "List Item 1",
            "List Item 2",
            "Paragraph 2.",
            "Ordered Item 1"
        ]
        self.assertEqual(split_by_html_tags(input_string), expected_output)

    def test_no_tags(self):
        input_string = "Just some plain text."
        expected_output = ["Just some plain text."]
        self.assertEqual(split_by_html_tags(input_string), expected_output)