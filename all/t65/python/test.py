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