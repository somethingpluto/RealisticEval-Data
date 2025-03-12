from typing import List

def find_duplicates_excluding_ips(ip_list: List[str], ignore_list: List[str]) -> List[str]:
    """
    Find duplicate IPs in the given IP list excluding specified IPs to ignore.

    Args:
        ip_list (List[str]): List of IP addresses
        ignore_list (List[str]): List of IP addresses to ignore

    Returns:
        List[str]: A list of duplicate IPs excluding those in the ignore list.
    """
    duplicates = []
    seen = set()
    
    for ip in ip_list:
        if ip in seen and ip not in ignore_list:
            duplicates.append(ip)
        else:
            seen.add(ip)
    
    return duplicates
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