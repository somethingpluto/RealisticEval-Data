import re


def replace_phone_numbers(text):
    # Define a regex pattern to match phone numbers
    # This pattern matches optional country codes, spaces, dashes, and brackets commonly found in phone numbers
    phone_pattern = r'\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b'

    # Replace all matches in the text with [PHONE_NUM]
    replaced_text = re.sub(phone_pattern, '[PHONE_NUM]', text)

    return replaced_text
