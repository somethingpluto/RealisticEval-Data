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
