def rename_png_files_in_directory(directory: str):
    """
    Renames PNG files in a specified directory by appending a sequence number to each file.
    The files are sorted alphabetically, and each base name is assigned sequential numbers.
    For example:
        director have three PNG files such as "image1.png", "image2.png", "image3.png"
        after renaming PNG files are "image1001.png", "image2001.png", "image3001.png"

    Args:
        directory (str): The path to the directory containing PNG files to be renamed.

    Returns:
        None
    """
