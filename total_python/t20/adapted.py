import re


def process_markdown_content(content):
    # Regular expression to find asterisks with spaces and characters in between
    pattern = r"\*[^*]*\*"

    # Function to remove spaces near asterisks within the found patterns
    def remove_extra_stars(match):
        # Remove spaces right after an opening asterisk and right before a closing asterisk
        return match.group().replace(" *", "*").replace("* ", "*")

    # Apply the function to all occurrences in the content
    processed_content = re.sub(pattern, remove_extra_stars, content)
    return processed_content
