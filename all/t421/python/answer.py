import os


def display_tree(dir_path, indent=''):
    """
    Recursively displays the file and directory structure under the specified directory path.

    Args:
    - dir_path (str): The path to the directory whose contents are to be displayed.
    - indent (str): The indentation string used to display the tree structure levels.
    """
    # Get all entries in the directory sorted by name
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        print(indent + "Permission denied.")
        return
    except FileNotFoundError:
        print(indent + "Directory not found.")
        return

    # Iterate over each item in the sorted list of directory contents
    for index, item in enumerate(items):
        # Determine the full path of the item
        full_path = os.path.join(dir_path, item)

        # Check if the item is the last in the list to adjust the tree branch
        if index == len(items) - 1:
            print(indent + '└── ' + item)
            next_indent = indent + '    '
        else:
            print(indent + '├── ' + item)
            next_indent = indent + '│   '

        # If the item is a directory, recurse into it
        if os.path.isdir(full_path):
            display_tree(full_path, next_indent)