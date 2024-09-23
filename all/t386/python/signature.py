import shutil


def convert_encoding(input_file_path: str, output_file_path: str, original_encoding="cp932",
                     target_encoding="utf_16") -> bool:
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
