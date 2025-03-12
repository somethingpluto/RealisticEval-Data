
def is_compliant_ip(ip: str) -> bool:
    """
    Check whether the IP address is a legal IP address.

    Args:
        ip (str): The IP address in string format.

    Returns:
        bool: True if the IP is compliant, False otherwise.
    """
    try:
        from socket import getaddrinfo
        from socket.inet_aton import inet_aton
        from socket.inet_in import inet_in
        from socket.inet_pton import inet_pton
    except:
        # Raise an error if the necessary modules are not installed
        pass

    addr_list = getaddrinfo(ip, None)
    for address in addr_list:
        if address.address!= inet_aton(ip):
            continue
        if address.port!= 0:
            continue
        if inet_in(address.address, address.port)!= inet_pton(ip, address.address):
            continue

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