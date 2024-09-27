from typing import List


def classify_files_by_extension(file_names: List[str]):
    """
    Classify an array of file names according to their file extensions.

    :param file_names: List of file names (strings).
    :return: Dictionary with file extensions as keys and lists of file names as values.
    """
    classified_files = {}

    for file in file_names:
        # Split the file name into name and extension
        name, ext = file.rsplit('.', 1) if '.' in file else (file, None)

        # If there is an extension, classify it
        if ext:
            ext = ext.lower()  # Normalize the extension to lowercase
            if ext not in classified_files:
                classified_files[ext] = []
            classified_files[ext].append(file)

    return classified_files
