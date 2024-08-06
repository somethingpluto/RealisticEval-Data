import re


def simplify_path(path: str) -> str:
    """
    Simplify filesystem paths to name strings on different systems.For example in windows , D:\downlaod\text.py to D_download_text.py on windows,in linux /home/user/test.py to home_user_test.py
    Args:
        path (str):

    Returns: simple path str

    """
    simplified = path.replace('\\', '_').replace('/', '_').replace(':', '_')

    # Removing illegal characters that cannot be used in file names across various systems
    illegal_chars = ['<', '>', '|', '?', '*', '"']
    for char in illegal_chars:
        simplified = simplified.replace(char, '_')

    # Special handling to remove a leading underscore if the path starts with a slash
    # This is typically relevant for Unix/Linux paths
    if path.startswith('/') or path.startswith('\\'):
        simplified = simplified.lstrip('_')

    return simplified