import PyPDF2


def extract_text_from_pdf(file_path):
    """
    Extracts text from a given PDF file.

    Args:
    file_path (str): The path to the PDF file from which to extract text.

    Returns:
    str: The extracted text from the PDF.
    """
    # Initialize a text container
    extracted_text = ""

    # Open the PDF file
    with open(file_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from each page and add it to the text container
            extracted_text += page.extract_text() + "\n"

    return extracted_text
