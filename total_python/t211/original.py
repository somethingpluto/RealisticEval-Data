import re


def extract_parameters_from_file(file_path):
    """
    Extract parameters, descriptions, and units from a Fortran file.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression pattern to capture potential parameter declarations
    pattern = r"\breal\(r8\)\s*,\s*target\s*,\s*allocatable\s*::\s*(\w+)\s*(?:\((.*?)\))?\s*!\s*(.*?)\s*,\s*\[(.*?)\]"
    matches = re.findall(pattern, content, re.IGNORECASE)

    # Extract parameters, descriptions, and units
    extracted_data = [{"variable_name": match[0].strip(),
                       "description": match[2].strip(),
                       "units": match[3].strip()}
                      for match in matches]

    return extracted_data
