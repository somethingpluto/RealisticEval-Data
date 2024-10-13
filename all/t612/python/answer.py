def find_and_replace_in_file(file_path, search_string, replace_string):
    """Finds and replaces text in a specified file.

    Args:
        file_path (str): The path to the file.
        search_string (str): The string to search for.
        replace_string (str): The string to replace with.

    Raises:
        IOError: If an I/O error occurs reading from the file or writing to the file.
    """
    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Replace the search string with the replacement string
        replaced_content = file_content.replace(search_string, replace_string)

        # Write the replaced content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(replaced_content)

    except IOError as e:
        print(f"Error occurred: {e}")