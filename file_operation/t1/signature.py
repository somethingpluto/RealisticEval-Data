import os
import json


def merge_json_list_data(input_dir: str, output_json: str) -> None:
    """
    Reads all the JSON files from the specified directory and merges the data in those files into a list
    :param input_dir: json file dir path
    :param output_json:
    :return:
    """