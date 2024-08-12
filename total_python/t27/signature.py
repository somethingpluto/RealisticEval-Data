import os
import json
from typing import List


def concatenate_json_arrays(directory: str) -> List:
    """
    concatenate the root-level array JSON files in the specified directory
    Args:
        directory (str): directory dir path

    Returns: merged data

    """
