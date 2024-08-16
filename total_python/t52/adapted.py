import os


def rename_files_in_directory(directory):
    """
    Rename all files in the specified directory by replacing colons in the filenames with hyphens.

    Args:
    directory (str): The path to the directory containing the files to be renamed.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The specified directory does not exist: {directory}")

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory or link etc.)
        if os.path.isfile(file_path):
            # Replace colons in the filename with hyphens
            new_filename = filename.replace(':', '-')

            # Construct the new file path
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
