import re


def is_cpp_header_file(file_name: str) -> bool:
    """
    Checks whether a file name is a C++ header file.

    Args:
        file_name (str): The name of the file to check.

    Returns:
        bool: Returns True if the file is a C++ header file, False otherwise.
    """
    # Define a regular expression to match C++ header file extensions
    cpp_header_extensions = re.compile(r'\.(h|hh|hpp|hxx)$', re.IGNORECASE)

    # Test the file name against the regular expression
    return bool(cpp_header_extensions.search(file_name))
