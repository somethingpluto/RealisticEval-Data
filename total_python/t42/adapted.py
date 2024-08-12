import re


def replace_phone_numbers(text):
    # Define a regex pattern to match phone numbers
    # This pattern matches optional country codes, spaces, dashes, and brackets commonly found in phone numbers
    phone_pattern = r"\+?\d{1,3}[-\s]?(?:\(\d{1,3}\)[-.\s]?)?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}"

    # Replace all matches in the text with [PHONE_NUM]
    replaced_text = re.sub(phone_pattern, '[PHONE_NUM]', text)

    return replaced_text
