from typing import List
from collections import Counter

def find_duplicates_excluding_ips(ip_list: List[str], ignore_list: List[str]) -> List[str]:
    """
    Find duplicate IPs in the given IP list excluding specified IPs to ignore.

    Args:
        ip_list (List[str]): List of IP addresses
        ignore_list (List[str]): List of IP addresses to ignore

    Returns:
        List[str]: A list of duplicate IPs excluding those in the ignore list.
    """
    # Create a counter of IPs
    ip_counter = Counter(ip_list)

    # Filter out IPs that are in the ignore list
    ip_counter = {ip: count for ip, count in ip_counter.items() if ip not in ignore_list}

    # Find the duplicate IPs
    duplicate_ips = [ip for ip, count in ip_counter.items() if count > 1]

    return duplicate_ips
import unittest


class TestFindDuplicateIPs(unittest.TestCase):

    def test_basic_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])

    def test_ignored_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "192.168.1.2"]
        ignore_list = ["192.168.1.1"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_no_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_mixed_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "10.0.0.1", "192.168.1.2"]
        ignore_list = ["192.168.1.2"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])

    def test_empty_input(self):
        ip_list = []
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_only_ignored_ips(self):
        ip_list = ["192.168.1.1", "192.168.1.1"]
        ignore_list = ["192.168.1.1"]
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), [])

    def test_all_duplicates(self):
        ip_list = ["192.168.1.1", "192.168.1.1", "192.168.1.1"]
        ignore_list = []
        self.assertEqual(find_duplicates_excluding_ips(ip_list, ignore_list), ["192.168.1.1"])
if __name__ == '__main__':
    unittest.main()