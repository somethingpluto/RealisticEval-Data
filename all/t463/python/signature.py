import re


def extract_log_levels(log_file_path:str, output_file_path:str):
    """
    Obtain logs of [WARNING], [ERROR], [CRITICAL], and [ALERT] levels from the log file
    log content such as:
        [INFO] Information message
        [WARNING] Warning message
        [DEBUG] Debug message

    Args:
        log_file_path: log file path
        output_file_path: output log file path

    Returns:

    """