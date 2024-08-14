import unittest


class TestIsCompliantIP(unittest.TestCase):
    def test_private_ip(self):
        # Test that private IPs return True
        self.assertTrue(is_compliant_ip('192.168.1.1'))

    def test_public_ip(self):
        # Test that public IPs return False
        self.assertFalse(is_compliant_ip('8.8.8.8'))

    def test_invalid_ip(self):
        # Test that invalid IP strings return False
        self.assertFalse(is_compliant_ip('999.999.999.999'))

    def test_ipv6_private(self):
        # Test an IPv6 private address
        self.assertTrue(is_compliant_ip('fd00::'))

    def test_ipv6_public(self):
        # Test an IPv6 public address
        self.assertFalse(is_compliant_ip('2001:4860:4860::8888'))
import ipaddress


def is_compliant_ip(ip):
    """
    Check if the given IP address is compliant based on predefined criteria.

    Args:
    ip (str): The IP address in string format.

    Returns:
    bool: True if the IP is compliant, False otherwise.
    """
    try:
        # Convert the input string to an IP address object
        ip_obj = ipaddress.ip_address(ip)

        # Check compliance criteria: for example, whether the IP is private
        # You can modify or extend this check based on other criteria, e.g., ip_obj.is_global, ip_obj.is_multicast, etc.
        return ip_obj.is_private

    except ValueError:
        # If the input is not a valid IP address, it cannot be compliant
        return False
