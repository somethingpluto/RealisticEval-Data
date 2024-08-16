import os
import shutil


def empty_directory(directory_path):
    """
    Empties all files and subdirectories in the specified directory, but keeps the directory itself.

    Args:
    directory_path (str): Path to the directory whose contents are to be emptied.

    Raises:
    ValueError: If the specified path does not exist or is not a directory.
    """
    # Check if the path exists and is a directory
    if not os.path.exists(directory_path):
        raise ValueError("The specified directory does not exist.")
    if not os.path.isdir(directory_path):
        raise ValueError("The specified path is not a directory.")

    # Iterate over all items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Check if the item is a file or directory and delete accordingly
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)  # Remove the file or link
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove the directory and all its contents
