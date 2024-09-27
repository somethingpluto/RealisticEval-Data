import re


def extract_bib_info(bib_file):
    """Extracts the title, author, and year from a BibTeX file.

    Args:
        bib_file (str): The path to the BibTeX file.

    Returns:
        list of dict: A list containing dictionaries with title, author, and year for each article.
    """
    articles = []

    # Regular expressions to match title, author, and year
    title_pattern = re.compile(r'title\s*=\s*{([^}]*)}', re.IGNORECASE)
    author_pattern = re.compile(r'author\s*=\s*{([^}]*)}', re.IGNORECASE)
    year_pattern = re.compile(r'year\s*=\s*{([^}]*)}', re.IGNORECASE)

    try:
        with open(bib_file, 'r') as file:
            content = file.read()

            # Split the content into individual entries based on '@'
            entries = content.split('@')[1:]  # Skip the first split, which is empty

            for entry in entries:
                title = title_pattern.search(entry)
                author = author_pattern.search(entry)
                year = year_pattern.search(entry)

                # Extracting matched groups if found
                articles.append({
                    'title': title.group(1) if title else None,
                    'author': author.group(1) if author else None,
                    'year': year.group(1) if year else None
                })

    except FileNotFoundError:
        print(f"Error: The file '{bib_file}' was not found.")

    return articles
