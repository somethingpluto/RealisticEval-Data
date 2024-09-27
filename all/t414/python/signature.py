def extract_bib_info(bib_file: str):
    """
    Extracts the title, author, and year from a BibTeX file.bib file content such as @article{sample2024,\n  author = {John Doe and Jane Smith},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}

    Args:
        bib_file (str): The path to the BibTeX file.

    Returns:
        list of dict: A list containing dictionaries with title, author, and year for each article.
    """
