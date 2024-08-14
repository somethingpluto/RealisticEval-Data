import os


def rename_files_in_folder(folder_path: str) -> None:
    """
    Rename all files in the specified folder, replacing colons in the file names with hyphens.

    :param folder_path: The path to the folder containing the files to rename.
    """
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file name contains a colon
        if ':' in filename:
            # Construct the new file name by replacing colons with hyphens
            new_filename = filename.replace(':', '-')
            # Construct full file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)