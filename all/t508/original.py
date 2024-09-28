import json

import numpy as np
import pandas as pd


class CustomJSONEncoder(json.JSONEncoder):
    """
    Generated with GPT-4. A fix for encoding a dict that may contain numpy_bool and dataframe.
    orient = "split" is to counter edge where if index is not unique, orient = "index" or "columns" causes ValueError

    Example use case:
        data = <a dictionary containing numpy.bool_ and pandas dataframe>

        with open(folder/file_name, "w") as op:
            json.dump(data, op, cls=CustomJSONEncoder)
    """
    def default(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, pd.DataFrame):
            return obj.to_json(orient="split" , indent=1)
        return json.JSONEncoder.default(self, obj)