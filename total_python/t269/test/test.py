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