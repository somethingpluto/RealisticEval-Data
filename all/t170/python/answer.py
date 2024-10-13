import re
def convert(html: str) -> str:
    # Replace line breaks
    markdown = re.sub(r'(?i)<br\s*/?>', '\n', html)
    # Replace paragraph tags
    markdown = re.sub(r'(?i)<p>', '', markdown)
    markdown = re.sub(r'(?i)</p>', '\n\n', markdown)
    # Replace strong and bold tags
    markdown = re.sub(r'(?i)<strong>', '**', markdown)
    markdown = re.sub(r'(?i)</strong>', '**', markdown)
    # Replace italic tags with emphasis
    markdown = re.sub(r'(?i)<em>', '*', markdown)
    markdown = re.sub(r'(?i)</em>', '*', markdown)
    # Replace underline (not native to markdown, commonly represented with emphasis)
    markdown = re.sub(r'(?i)<u>', '*', markdown)
    markdown = re.sub(r'(?i)</u>', '*', markdown)
    # Replace code tags
    markdown = re.sub(r'(?i)<code>', '`', markdown)
    markdown = re.sub(r'(?i)</code>', '`', markdown)
    # Replace unordered lists
    markdown = re.sub(r'(?i)<ul>', '', markdown)
    markdown = re.sub(r'(?i)</ul>', '', markdown)
    # Replace ordered lists
    markdown = re.sub(r'(?i)<ol>', '', markdown)
    markdown = re.sub(r'(?i)</ol>', '', markdown)
    # Replace list items
    markdown = re.sub(r'(?i)<li>', '* ', markdown)
    markdown = re.sub(r'(?i)</li>', '\n', markdown)
    # Correctly replace anchor tags in one pass
    markdown = re.sub(r'(?i)<a\s+href="([^"]*)">(.*?)</a>', r'[\2](\1)', markdown)
    
    return markdown