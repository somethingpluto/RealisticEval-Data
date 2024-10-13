def is_significant_number(input_value):
    # Check if input is a string
    if not isinstance(input_value, str):
        return False

    # Trim whitespace from the input
    input_value = input_value.strip()

    # Check the length
    length = len(input_value)
    if length < 5 or length > 18:
        return False

    # Check for significant number: all characters must be digits
    # and cannot start with '0' if the length is greater than 1
    if not input_value.isdigit() or (length > 1 and input_value[0] == '0'):
        return False

    return True
