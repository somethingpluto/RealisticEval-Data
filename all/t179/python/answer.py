import os
import shutil


def copy_directory(source_dir: str, target_dir: str) -> None:
    """
    Copies all files and subdirectories from the source directory to the target directory.

    :param source_dir: The source directory from which files and subdirectories will be copied.
    :param target_dir: The target directory to which files and subdirectories will be copied.
    :raises ValueError: If the source directory does not exist or is not a directory.
    """
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source is not a directory: {source_dir}")

    os.makedirs(target_dir, exist_ok=True)  # Create target directory if it doesn't exist

    # Copy each file and directory in the source directory
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        if os.path.isdir(source_path):
            # Recursively copy the subdirectory
            copy_directory(source_path, target_path)
        else:
            # Copy the file
            copy_file(source_path, target_path)


def copy_file(source: str, target: str) -> None:
    """
    Copies a single file from the source path to the target path.

    :param source: The source file path.
    :param target: The target file path.
    :raises IOError: If an I/O error occurs during file copy.
    """
    shutil.copy2(source, target)  # Copy the file and preserve metadata
