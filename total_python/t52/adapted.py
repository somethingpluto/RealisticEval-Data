import os

def rename_files(directory_path):
    """
    Recursively renames files within a given directory by replacing colons in filenames with dashes.

    Parameters:
    - directory_path (str): The path to the directory where files will be renamed.

    Returns:
    - None
    """
    # Walk through all subdirectories of the provided directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Construct the full path of the current file
            old_file_path = os.path.join(root, file)
            # Replace colons with dashes in the filename
            new_file_name = file.replace(':', '-')
            new_file_path = os.path.join(root, new_file_name)

            # Only attempt to rename if the new name is different from the old name
            if old_file_path != new_file_path:
                try:
                    # Perform the file rename
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{old_file_path}' to '{new_file_path}'")
                except OSError as error:
                    # Handle potential errors during the rename operation, e.g., file being used by another process
                    print(f"Error renaming '{old_file_path}' to '{new_file_path}': {error}")