def clean_dictionary(input_dict):
    """
    Cleans the input dictionary by removing keys with invalid values.
    Valid values are non-NaN, non-None, and non-whitespace strings.

    :param input_dict: A dictionary to be cleaned.
    :return: A new dictionary containing only valid values.
    """
    cleaned_dict = {}

    for key, value in input_dict.items():
        # Check if the value is not None and not NaN and not a whitespace string
        if value is not None and (isinstance(value, str) and value.strip() != ""):
            # Check if value is a number (int or float) and is not NaN
            if not (isinstance(value, float) and np.isnan(value)):
                cleaned_dict[key] = value

    return cleaned_dict
