import re


def process_markdown(content):
    # Regular expression to find and correct the asterisk patterns
    # This pattern assumes there are no nested asterisks that need to be considered
    corrected_content = re.sub(r'\*(.+?)\*', lambda m: '*' + m.group(1).replace('*', '') + '*', content)

    return corrected_content
