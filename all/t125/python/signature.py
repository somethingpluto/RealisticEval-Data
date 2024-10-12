def compress_html(html_string: str) -> str:
    """
    Compresses an HTML string by removing unnecessary whitespace without disrupting
    the integrity of content within <pre>, <div>, <script>, and <style> tags.

    For example:
        input: '   <div>   Content  </div>   '
        output: '<div> Content </div>'

    Args:
        html_string (str): The HTML content to compress.

    Returns:
        str: The compressed HTML content.
    """