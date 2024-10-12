import re

def compress_html(html):
    # Remove leading/trailing whitespace around tags
    html = re.sub(r'\s*(<[^>]+>)\s*', r'\1', html)
    # Remove multiple newlines and replace with a single space
    html = re.sub(r'\n+', ' ', html)
    # Remove multiple spaces and replace them with a single space
    html = re.sub(r'[ \t]+', ' ', html)
    return html.strip()
