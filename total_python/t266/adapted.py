def handle_nested_data(data):
    if isinstance(data, dict):
        # If it's a dictionary, apply the function recursively to each value
        return {key: handle_nested_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        # If it's a list, apply the function recursively to each item
        return [handle_nested_data(item) for item in data]
    elif isinstance(data, bytes):
        # If it's bytes, decode to a UTF-8 string
        return data.decode('utf-8')
    elif isinstance(data, (int, float)):
        # If it's already a number, return as is
        return data
    elif isinstance(data, str):
        # Try to convert strings that represent integers or floats to their numeric forms
        try:
            return int(data)
        except ValueError:
            try:
                return float(data)
            except ValueError:
                return data  # Return the original string if it's not a number
    return data  # Return the data as is for any other type