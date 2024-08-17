import json


class BitSequenceEncoder(json.JSONEncoder):
    """
    Custom JSON encoder class that converts dictionary entries with the key 'bits'
    into a binary string format.

    This encoder transforms only those entries in a dictionary where the key is 'bits',
    formatting their values as 8-bit binary strings. Other entries are left unchanged.
    """

    def default(self, obj):
        """
        Overridden method from json.JSONEncoder to provide custom encoding logic.

        Args:
            obj (any): The object to encode.

        Returns:
            any: The encoded object or super().default(obj) for types unsupported by this encoder.
        """

        # Helper function to recursively convert dictionary entries
        def convert_bits(item):
            if isinstance(item, dict):
                # Transform the dictionary, applying binary formatting if the key is 'bits'
                return {k: (f'{v:08b}' if k == 'bits' else convert_bits(v)) for k, v in item.items()}
            elif isinstance(item, list):
                # Apply conversion to each element in the list
                return [convert_bits(v) for v in item]
            else:
                # Return the item unchanged if it's not a dictionary or list
                return item

        # Use the helper function to process the top-level object
        return convert_bits(obj)
