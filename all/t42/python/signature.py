def replace_phone_numbers(text: str):
    """
    replace all phones(phone formats in many) in the string with the string [PHONE_NUM]
    For example:
        input: Call me at 123-456-7890.
        output: Call me at [PHONE_NUM].

    Args:
        text (str): The input string that may contain phone numbers.

    Returns:
        str: The modified string with phone numbers replaced by '[PHONE_NUM]'.
    """
