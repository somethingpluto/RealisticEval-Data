from typing import List


def find_duplicate_ips(ip_list: List[str], ignore_list: List[str]) -> List[str]:
    """
    Find duplicate IPs in the given IP list excluding specified IPs to ignore.

    Args:
        ip_list (List[str]): List of IP addresses
        ignore_list (List[str]): List of IP addresses to ignor

    Returns:
        List[str]: A list of duplicate IPs excluding those in the ignore list.
    """
