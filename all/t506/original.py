def to_camel_case(input_string: str) -> str:
    """
    Converts snake_case strings into CamelCase (created by ChatGPT)
    :param input_string: String to convert
    :return: String converted to CamelCase
    """
    words = input_string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
