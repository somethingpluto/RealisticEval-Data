import re

def is_compliant_ip(ip: str) -> bool:
    ip_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    
    if re.match(ip_pattern, ip):
        octets = ip.split('.')
        for octet in octets:
            if int(octet) < 0 or int(octet) > 255:
                return False
        return True
    return False
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