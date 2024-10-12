import re
from typing import Dict, List

def parse_categories_from_summary(summarized_output: str = '') -> Dict[str, List[str]]:
    """
    Extracts categories from a summarized output string and returns the cleaned summary and categories.
    The categories are expected to be in the format "Categories: [category1, category2, ...]".

    Args:
        summarized_output (str): The summary text potentially containing categorized question.

    Returns:
        dict: A dictionary containing the cleaned summary text and a list of categories.
    """
    # Define the regex to find the categories pattern in the summary
    categories_regex = r'Categories:\s*\[([^\]]+)\]'
    
    # Attempt to match the pattern
    match = re.search(categories_regex, summarized_output, re.IGNORECASE)
    categories = []
    summary = summarized_output

    # If a match is found, process the categories and clean the summary
    if match and match.group(1):
        # Extract and process categories
        categories = [category.strip() for category in match.group(1).split(',') if category.strip()]

        # Remove the category line from the summary and trim any leading/trailing whitespace
        summary = re.sub(categories_regex, '', summarized_output).strip()

    return {'summary': summary, 'categories': categories}