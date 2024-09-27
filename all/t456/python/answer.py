import re


def split_by_html_tags(html_content):
    """
    Splits the provided HTML content string by <p>, <ul>, and <ol> tags.

    Parameters:
        html_content (str): A string containing HTML content.

    Returns:
        list: A list of strings, split by <p>, <ul>, and <ol> tags.
    """
    # Pattern to find <p>, <ul>, <ol> and their corresponding closing tags
    pattern = re.compile(r'(<p>|</p>|<ul>|</ul>|<ol>|</ol>)')

    # Split the html content by the pattern
    parts = pattern.split(html_content)

    # Filter out empty strings and return the result
    return [part for part in parts if part.strip()]