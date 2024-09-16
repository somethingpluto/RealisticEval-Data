import unittest
from unittest.mock import patch, MagicMock


class TestExtractTextFromWord(unittest.TestCase):

    @patch('docx.Document')
    def test_normal_case(self, mock_document):
        mock_doc = MagicMock()
        mock_doc.paragraphs = [MagicMock(text="This is the first paragraph."),
                               MagicMock(text="This is the second paragraph.")]
        mock_document.return_value = mock_doc

        docx_path = "dummy.docx"
        expected_output = "This is the first paragraph.\nThis is the second paragraph."

        result = extract_text_from_word(docx_path)
        self.assertEqual(result, expected_output)

    @patch('docx.Document')
    def test_empty_document(self, mock_document):
        mock_doc = MagicMock()
        mock_doc.paragraphs = []
        mock_document.return_value = mock_doc

        docx_path = "dummy.docx"
        expected_output = ""

        result = extract_text_from_word(docx_path)
        self.assertEqual(result, expected_output)

    @patch('docx.Document')
    def test_special_characters(self, mock_document):
        mock_doc = MagicMock()
        mock_doc.paragraphs = [MagicMock(text="Special characters: \n\t© 2023.")]
        mock_document.return_value = mock_doc

        docx_path = "dummy.docx"
        expected_output = "Special characters: \n\t© 2023."

        result = extract_text_from_word(docx_path)
        self.assertEqual(result, expected_output)

    @patch('docx.Document')
    def test_single_paragraph(self, mock_document):
        mock_doc = MagicMock()
        mock_doc.paragraphs = [MagicMock(text="This document has a single paragraph.")]
        mock_document.return_value = mock_doc

        docx_path = "dummy.docx"
        expected_output = "This document has a single paragraph."

        result = extract_text_from_word(docx_path)
        self.assertEqual(result, expected_output)

    @patch('docx.Document')
    def test_document_with_only_whitespace(self, mock_document):
        mock_doc = MagicMock()
        mock_doc.paragraphs = [MagicMock(text="    "), MagicMock(text="\t\t")]
        mock_document.return_value = mock_doc

        docx_path = "dummy.docx"
        expected_output = "    \n\t\t"

        result = extract_text_from_word(docx_path)
        self.assertEqual(result, expected_output)
