import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Override the default() method to encode specific data types.

        Args:
        obj (any): The object to encode.

        Returns:
        any: A JSON-serializable form of the object or calls the base class's default method.
        """
        # Handle dictionary specially to convert certain keys
        if isinstance(obj, dict):
            new_obj = {}
            for key, value in obj.items():
                # Check if the key indicates a value that should be converted to binary
                if key == 'bits' and isinstance(value, int):
                    # Convert integer to a binary string
                    new_obj[key] = bin(value)[2:]  # bin() returns a string starting with '0b'
                else:
                    # Recursively handle all other values normally
                    new_obj[key] = value
            return new_obj
        # Use the default method for any other type not explicitly handled
        return super().default(obj)
