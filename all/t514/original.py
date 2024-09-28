import re


def process_date(file_name):
    pattern = r'\d{4}-\d{2}-\d{2}'
    # Use re.search to find the match
    match = re.search(pattern, file_name)
    if match:
        # Extract the matched date
        date_str = match.group(0)
        return date_str