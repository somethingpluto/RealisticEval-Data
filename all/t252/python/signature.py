import json


class BitSequenceEncoder(json.JSONEncoder):
    """
    Write a JSON decoding class that inherits from json.JSONEncoder. When encoding question into json format, the main functional bits of this class specifically handle keys identified as bits, and convert them to binary form if their value is an integer
    For example 'bits': 255 after encoder "bits": "11111111"

    """

    def encode(self, obj):
        pass
