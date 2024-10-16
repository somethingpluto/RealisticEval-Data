import os
import re
from pathlib import Path


def rename_png_files_in_directory(directory):
    """
    Renames PNG files in a specified directory by appending a sequence number to each file.
    The files are sorted alphabetically, and each base name is assigned sequential numbers.

    Args:
        directory (str): The path to the directory containing PNG files to be renamed.

    Returns:
        None
    """
    # Convert directory to Path object for easier handling
    dir_path = Path(directory)

    if not dir_path.exists() or not dir_path.is_dir():
        raise ValueError(f"The directory '{directory}' does not exist or is not a directory.")

    # Get list of PNG files in the directory
    png_files = [f for f in dir_path.iterdir() if f.is_file() and f.suffix.lower() == '.png']

    # Sort files alphabetically by their names
    png_files.sort()

    # Print the sorted list of files (for debugging)
    print("Sorted files:")
    for file in png_files:
        print(file.name)

    # Rename files with sequence numbers
    prev_base_name = None
    count = 1

    for file in png_files:
        # Extract base name without postfix and number
        base_name = re.sub(r'(\d{3})(-\d)?(?=\.png$)', '', file.stem)

        if base_name != prev_base_name:
            count = 1

        new_filename = f"{base_name}{count:03d}.png"
        new_file_path = file.with_name(new_filename)
        os.rename(file, new_file_path)
        print(f"Renaming {file.name} to {new_filename}")

        prev_base_name = base_name
        count += 1
