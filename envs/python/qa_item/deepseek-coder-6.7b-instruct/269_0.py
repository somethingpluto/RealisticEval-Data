import re

def is_compliant_ip(ip: str) -> bool:
    """
    Check whether the IP address is a legal IP address.

    Args:
        ip (str): The IP address in string format.

    Returns:
        bool: True if the IP is compliant, False otherwise.
    """
    # Regular expression pattern for a valid IPv4 address
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    
    # Match the IP address against the pattern
    match = re.match(ipv4_pattern, ip)
    
    if not match:
        return False
    
    # Check each octet to ensure it is between 0 and 255
    for octet in match.groups():
        if not (0 <= int(octet) <= 255):
            return False
    
    return True
import unittest


class TestIsCompliantIP(unittest.TestCase):
    def test_private_ip(self):
        # Test that private IPs return True
        self.assertTrue(is_compliant_ip('192.168.1.1'))

    def test_public_ip(self):
        # Test that public IPs return False
        self.assertTrue(is_compliant_ip('8.8.8.8'))

    def test_invalid_ip(self):
        # Test that invalid IP strings return False
        self.assertFalse(is_compliant_ip('999.999.999.999'))

if __name__ == '__main__':
    unittest.main()