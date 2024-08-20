from typing import List, Dict


def extract_parameters_from_file(file_path:str) -> List[Dict]:
    """
    extract the names, descriptions, and units of the parameters from a Fortran file, put this information in the form of a list, where each element is a dictionary, and return the list

    Args:
        file_path (str): Path to the Fortran file.

    Returns:
        list of dict: A list of dictionaries, each containing the variable name,
                  description, and units of a parameter.

    """
