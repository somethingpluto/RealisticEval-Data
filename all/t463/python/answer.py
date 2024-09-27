import re


def extract_log_levels(log_file_path, output_file_path):
    # Define the regex pattern to match log levels
    log_pattern = re.compile(r'\[(WARNING|ERROR|CRITICAL|ALERT)\]')

    with open(log_file_path, 'r') as file:
        with open(output_file_path, 'w') as output:
            # Iterate over each line in the log file
            for line in file:
                # Check if the line contains any of the log levels
                if log_pattern.search(line):
                    # If it does, write this line to the output file
                    output.write(line)
