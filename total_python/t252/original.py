import json


class BitSequenceEncoder(json.JSONEncoder):
    """
    Function to override the default json encoder to show register data in binary.
    Note: This function was generated using ChatGPT-4o on July 15, 24. Might behave unexpectedly.
    """
    def encode(self, obj):
        def convert_bits(item):
            if isinstance(item, dict):
                return {k: convert_bits(v) if k != 'bits' else f'{v:08b}' for k, v in item.items()}
            return item

        converted_obj = convert_bits(obj)
        return super(BitSequenceEncoder, self).encode(converted_obj)