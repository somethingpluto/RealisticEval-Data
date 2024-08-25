import re


def extract_parameters_from_file(file_path):
    """
    Extract parameters, descriptions, and units from a Fortran file.

    Args:
    file_path (str): Path to the Fortran file.

    Returns:
    list of dict: A list of dictionaries, each containing the variable name,
                  description, and units of a parameter.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    """
    # Open the file safely, handling the file not found error
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")

    # Regular expression pattern to capture parameter declarations
    pattern = (
        r"\breal\(r8\)\s*,\s*target\s*,\s*allocatable\s*::\s*"
        r"(\w+)\s*(?:\((.*?)\))?\s*!\s*(.*?)\s*,\s*\[(.*?)\]"
    )
    matches = re.findall(pattern, content, re.IGNORECASE)

    # Create a list of dictionaries for each match
    extracted_data = [
        {
            "variable_name": match[0].strip(),
            "dimensions": match[1].strip() if match[1] else None,
            "description": match[2].strip(),
            "units": match[3].strip()
        }
        for match in matches
    ]

    return extracted_data
