import json


class CustomJSONEncoder(json.JSONEncoder):
    """
    Custom JSON Encoder that converts Boolean values to 1 and 0.
    """
    def default(self, obj):
        if isinstance(obj, bool):
            return 1 if obj else 0
        return super().default(obj)