from docx import Document

def extract_text_from_word(docx_file_path):
    """
    Extracts text content from a given Word file (.docx).

    Args:
        docx_file_path (str): The path to the Word file.

    Returns:
        str: The extracted text content.
    """
    try:
        # Open the Word document
        doc = Document(docx_file_path)
        # Extract text from each paragraph in the document
        text_content = []
        for para in doc.paragraphs:
            text_content.append(para.text)

        # Join the paragraphs with newlines
        return '\n'.join(text_content)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None