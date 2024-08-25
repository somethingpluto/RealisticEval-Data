from typing import Dict, List


def find_duplicate_ips(files: List[str], ignored_ips: set) -> Dict:
    """
    find duplicate IP addresses across multiple files, excluding any IPs in the ignored list.
    Args:
        files (list): List of file paths to search.
        ignored_ips (set): Set of IP addresses to ignore.

    Returns:
        dict: A dictionary where each key is a duplicated IP address and the value is a list of filenames where the IP appears.
    """
