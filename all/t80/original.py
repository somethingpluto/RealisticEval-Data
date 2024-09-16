'''
    written by ChatGPT
    formats a string into a proper file name into a proper filename in windows
    @input_str: a string to be formatted
    @return: formatted_str, a formatted string stripped of special characters and spaces
'''
def format_windows_filename(input_str, replacement_char='_'):
    # Define a regex pattern for characters not allowed in Windows file names
    illegal_chars = re.compile(r'[<>:"/\\|?*]')

    # Replace illegal characters with the specified replacement character
    formatted_str = re.sub(illegal_chars, replacement_char, input_str)

    # Remove leading and trailing spaces
    formatted_str = formatted_str.strip()

    # Ensure the file name is not empty after replacement
    if not formatted_str:
        formatted_str = replacement_char

    return formatted_str