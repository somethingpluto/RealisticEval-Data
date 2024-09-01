from docx import Document


def extract_text_from_word(docx_path: str) -> str:
    """
    Extract text content from a given Word (.docx) file.

    Parameters:
    - docx_path (str): Path to the .docx file.

    Returns:
    - str: The extracted text content from the Word file.
    """
    try:
        # Open the Word document
        doc = Document(docx_path)
        # Extract text from each paragraph in the document
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        # Join all paragraphs into a single string
        return '\n'.join(full_text)

    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return ""
