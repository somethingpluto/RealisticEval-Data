import unittest
from unittest.mock import patch, MagicMock


class TestExtractAndChunkText(unittest.TestCase):

    @patch('fitz.open')
    def test_normal_case(self, mock_open):
        mock_page = MagicMock()
        mock_page.get_text.return_value = "This is a simple test case with multiple words to chunk."
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_open.return_value.__enter__.return_value = mock_doc

        pdf_path = "dummy.pdf"
        chunk_size = 5
        overlap = 0

        expected_output = [
            "This is a simple test",
            "case with multiple words",
            "to chunk."
        ]
        result = extract_and_chunk_text(pdf_path, chunk_size, overlap)
        self.assertEqual(result, expected_output)

    @patch('fitz.open')
    def test_overlap_case(self, mock_open):
        mock_page = MagicMock()
        mock_page.get_text.return_value = "Overlap test with some overlapping words in chunks."
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_open.return_value.__enter__.return_value = mock_doc

        pdf_path = "dummy.pdf"
        chunk_size = 5
        overlap = 2

        expected_output = [
            "Overlap test with some overlapping",
            "with some overlapping words in",
            "overlapping words in chunks."
        ]
        result = extract_and_chunk_text(pdf_path, chunk_size, overlap)
        self.assertEqual(result, expected_output)

    @patch('fitz.open')
    def test_empty_pdf(self, mock_open):
        mock_page = MagicMock()
        mock_page.get_text.return_value = ""
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_open.return_value.__enter__.return_value = mock_doc

        pdf_path = "dummy.pdf"
        chunk_size = 5
        overlap = 0

        expected_output = []
        result = extract_and_chunk_text(pdf_path, chunk_size, overlap)
        self.assertEqual(result, expected_output)

    @patch('fitz.open')
    def test_exact_chunk_fit(self, mock_open):
        mock_page = MagicMock()
        mock_page.get_text.return_value = "Exact chunk fit test case with perfect fit."
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_open.return_value.__enter__.return_value = mock_doc

        pdf_path = "dummy.pdf"
        chunk_size = 5
        overlap = 0

        expected_output = [
            "Exact chunk fit test case",
            "with perfect fit."
        ]
        result = extract_and_chunk_text(pdf_path, chunk_size, overlap)
        self.assertEqual(result, expected_output)

    @patch('fitz.open')
    def test_more_words_than_chunk_size(self, mock_open):
        mock_page = MagicMock()
        mock_page.get_text.return_value = "Small chunk size test case."
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_open.return_value.__enter__.return_value = mock_doc

        pdf_path = "dummy.pdf"
        chunk_size = 10
        overlap = 0

        expected_output = [
            "Small chunk size test case."
        ]
        result = extract_and_chunk_text(pdf_path, chunk_size, overlap)
        self.assertEqual(result, expected_output)


import fitz  # PyMuPDF
from typing import List


def extract_and_chunk_text(pdf_path: str, chunk_size: int, overlap: int) -> List[str]:
    """
    Extract text from a PDF file and chunk it into pieces.

    Parameters:
    - pdf_path (str): Path to the PDF file.
    - chunk_size (int): Number of words per chunk.
    - overlap (int): Number of overlapping words between consecutive chunks.

    Returns:
    - List[str]: List of text chunks extracted from the PDF.
    """
    texts = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            words = text.split()
            for i in range(0, len(words), chunk_size - overlap):
                chunk = ' '.join(words[i:i + chunk_size])
                texts.append(chunk)
    return texts
