import os
import re


def find_duplicate_ips(files, ignored_ips):
    """
    Find duplicate IP addresses across multiple files, excluding any IPs in the ignored list.

    Args:
    files (list): List of file paths to search.
    ignored_ips (set): Set of IP addresses to ignore.

    Returns:
    dict: A dictionary where each key is a duplicated IP address and the value is a list of filenames where the IP appears.
    """
    ip_regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    duplicates = {}

    for filename in files:
        # Check if the file exists before attempting to open
        if not os.path.isfile(filename):
            print(f"Skipping non-existent file: {filename}")
            continue

        with open(filename, "r") as file:
            for line in file:
                ips = re.findall(ip_regex, line)
                for ip in ips:
                    # Skip any IPs that are in the ignored list
                    if ip in ignored_ips:
                        continue

                    if ip not in duplicates:
                        duplicates[ip] = {filename}
                    else:
                        duplicates[ip].add(filename)

    # Convert sets to lists for consistent output
    return {ip: list(files) for ip, files in duplicates.items()}