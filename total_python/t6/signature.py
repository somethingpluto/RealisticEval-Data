def simplify_windows_path(path: str) -> str:
    """
    simplify file paths in windows systems into name strings, for example, D:\downlaod\text.py is simplified to D_download_text.py
    Args:
        path (str): windows file path str
    Returns:
        simplify path str
    """
