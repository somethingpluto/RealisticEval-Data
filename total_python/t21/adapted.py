import difflib


def compare_files(file1_path, file2_path):
    """
    Compare the contents of two files and print the differences in unified diff format.

    Args:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.

    Returns:
    list: A list containing the lines of differences, if any.

    Raises:
    FileNotFoundError: If either file does not exist.
    IOError: If there is an error reading the files.
    """
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("One of the files was not found.")
    except IOError as e:
        raise IOError(f"Error reading files: {e}")

    diff = difflib.unified_diff(lines1, lines2, fromfile=file1_path, tofile=file2_path)
    diff_lines = list(diff)

    for line in diff_lines:
        print(line, end="")

    return diff_lines
