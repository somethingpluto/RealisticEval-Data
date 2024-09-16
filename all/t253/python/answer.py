import json

def log(item):
    """
    Logs an item by printing it. Handles strings, numbers, lists, and dictionaries by printing
    them directly or as a JSON-formatted string. Other types are reported as errors.

    Args:
    item: The item to be logged. Can be of any type.
    """
    # Handling for strings, integers, and floats
    if isinstance(item, (str, int, float)):
        print(item)
    # Handling for dictionaries and lists to convert to JSON string
    elif isinstance(item, (dict, list)):
        try:
            print(json.dumps(item, indent=4))  # Pretty print JSON for better readability
        except TypeError as e:
            print(f"Error: Failed to serialize item to JSON. {e}")
    else:
        # Print an informative error message for unsupported types
        print(f"Error: Unsupported type {type(item).__name__} for logging.")