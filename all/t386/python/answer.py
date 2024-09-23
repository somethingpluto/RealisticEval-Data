import shutil


def convert_encoding(input_file_path, output_file_path, original_encoding="cp932", target_encoding="utf_16") -> bool:
    """
    This function converts the encoding of a file from one encoding to another

    Parameters:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to the output file where the converted content is saved.
        original_encoding (str): The original encoding of the file (default is cp932).
        target_encoding (str): The target encoding to convert to (default is utf_16).

    Returns:
        bool: True if the conversion was successful, or if no conversion was needed; False otherwise.
    """

    try:
        # Read the file with the original encoding
        with open(input_file_path, "r", encoding=original_encoding) as file:
            content = file.read()

        # Write the content in the new encoding
        with open(output_file_path, "w", encoding=target_encoding) as file:
            file.write(content)

        return True
    except UnicodeDecodeError as e:
        # Handle encoding errors if the file was already in the target encoding
        try:
            with open(input_file_path, "r", encoding=target_encoding) as file:
                file.read()  # Try reading to check if it's already in target encoding
            shutil.copyfile(input_file_path, output_file_path)  # Copy if no error occurs
            print(f"File already in target encoding: {input_file_path}")
            return True
        except UnicodeDecodeError:
            print(f"Conversion failed due to encoding error: {e}")
            return False
