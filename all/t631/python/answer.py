def write_csv_to_file(strings, file_path):
    """
    Formats a list of strings into a single-line CSV string and writes it to a specified file.

    :param strings: List of strings to be formatted into CSV.
    :param file_path: The file path where the CSV string should be written.
    """
    # Join the list of strings into a single line CSV formatted string
    csv_string = ','.join(strings)

    # Write the CSV string to the specified file
    try:
        with open(file_path, mode='w', newline='') as file:
            file.write(csv_string)
            print(f"CSV written to file: {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")