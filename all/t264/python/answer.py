import os


def extract_log_entries(log_file_path):
    """
    Extract log entries from a log file for WARNING, ERROR, CRITICAL, and ALERT levels
    and save each type of log entry to a different file.

    Args:
    log_file_path (str): Path to the log file.
    """
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"No log file found at the specified path: {log_file_path}")

    # Prepare dictionaries to hold log entries for each level
    logs = {
        'WARNING': [],
        'ERROR': [],
        'CRITICAL': [],
        'ALERT': []
    }

    # Define output file paths
    output_files = {
        'WARNING': 'warning_logs.txt',
        'ERROR': 'error_logs.txt',
        'CRITICAL': 'critical_logs.txt',
        'ALERT': 'alert_logs.txt'
    }

    # Read the log file and filter entries by level
    with open(log_file_path, 'r') as file:
        for line in file:
            for level in logs.keys():
                if level in line:
                    logs[level].append(line)
                    break

    # Write the filtered logs to separate files
    for level, entries in logs.items():
        with open(output_files[level], 'w') as outfile:
            outfile.writelines(entries)
            print(f"Saved {len(entries)} '{level}' entries to {output_files[level]}.")