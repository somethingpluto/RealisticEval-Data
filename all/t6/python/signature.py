def simplify_windows_path(path: str) -> str:
    """
    simplify file paths in windows systems into name strings.
    example:
       input C:\\Users\\User\\file.txt output C_Users_User_file.txt
    Args:
        path (str): windows file path str
    Returns:
        str: simplify path str
    """
