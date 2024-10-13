import os


def read_file_to_byte_array(file_path: str) -> bytes:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")

    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            if len(data) == 0:
                raise IOError(f"Could not completely read the file: {file_path}")
            return data
    except IOError as e:
        raise IOError(f"Error reading file: {e}")
