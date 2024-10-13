import shutil
import time


def copy_file_with_buffered_stream(source_file_path, destination_file_path):
    """
    Copies the contents of the source file to the destination file using a buffered stream
    and measures the time it takes to complete the operation.

    :param source_file_path: The path to the source file.
    :param destination_file_path: The path to the destination file.
    :return: The time taken to copy the file in milliseconds.
    """
    start_time = time.time()  # Start timing
    try:
        with open(source_file_path, 'rb') as source_file, \
                open(destination_file_path, 'wb') as destination_file:
            # Use shutil.copyfileobj to copy data in chunks
            shutil.copyfileobj(source_file, destination_file, length=8192)
    except IOError as e:
        print(f"Error: {e}")
        return None  # Return None in case of error

    end_time = time.time()  # End timing
    return (end_time - start_time) * 1000  # Convert to milliseconds