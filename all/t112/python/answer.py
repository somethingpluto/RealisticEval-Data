import re


def convert_html_headings_to_markdown(html: str) -> str:
    """
    Converts HTML heading tags (h1-h6) to corresponding Markdown headings.

    Args:
        html (str): The HTML string containing headings.

    Returns:
        str: The converted Markdown string.
    """
    # Replace h1 to h6 tags with corresponding Markdown headings
    html = re.sub(r'<h1>(.*?)<\/h1>', r'# \1', html)  # Converts <h1> to #
    html = re.sub(r'<h2>(.*?)<\/h2>', r'## \1', html)  # Converts <h2> to ##
    html = re.sub(r'<h3>(.*?)<\/h3>', r'### \1', html)  # Converts <h3> to ###
    html = re.sub(r'<h4>(.*?)<\/h4>', r'#### \1', html)  # Converts <h4> to ####
    html = re.sub(r'<h5>(.*?)<\/h5>', r'##### \1', html)  # Converts <h5> to #####
    html = re.sub(r'<h6>(.*?)<\/h6>', r'###### \1', html)  # Converts <h6> to ######

    return html