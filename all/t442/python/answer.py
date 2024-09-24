def convert_strings_to_numbers(data):
    if isinstance(data, dict):
        return {key: convert_strings_to_numbers(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_strings_to_numbers(item) for item in data]
    elif isinstance(data, str):
        try:
            # Try converting to float first, then to int if possible
            if '.' in data:
                return float(data)
            else:
                return int(data)
        except ValueError:
            return data  # Return original string if conversion fails
    else:
        return data  # Return data unchanged if it's not a string