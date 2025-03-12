import subprocess
import re
from typing import Optional

def get_local_ip(interface: str = 'Wi-Fi') -> Optional[str]:
    """
    Retrieve the local IP address of the specified network interface on Windows.

    Args:
        interface (str): The name of the network interface to check (default is 'Wi-Fi').

    Returns:
        Optional[str]: The local IP address if found, otherwise None.
    """
    ipconfig_result = subprocess.run(['ipconfig'], capture_output=True, text=True)
    ip_lines = ipconfig_result.stdout.split('\n')
    
    for line in ip_lines:
        if interface in line:
            ip_match = re.search(r'IPv4 Address[.]+:[ ]+([\d.]+)', line)
            if ip_match:
                return ip_match.group(1)
    
    return None
import subprocess
import unittest
from unittest.mock import patch, MagicMock


class TestGetLocalIP(unittest.TestCase):

    @patch('subprocess.run')
    def test_local_ip_found(self, mock_run):
        # Mock the output of ipconfig for a case where a local IP is found
        mock_run.return_value = MagicMock(stdout='192.168.1.10\n')
        result = get_local_ip()
        self.assertEqual(result, '192.168.1.10')

    @patch('subprocess.run')
    def test_no_local_ip_found(self, mock_run):
        # Mock the output of ipconfig for a case where no local IP is found
        mock_run.return_value = MagicMock(stdout='10.0.0.5\n')
        result = get_local_ip()
        self.assertIsNone(result)

    @patch('subprocess.run')
    def test_multiple_ips_found(self, mock_run):
        # Mock the output with multiple local IPs
        mock_run.return_value = MagicMock(stdout='10.0.0.5\n'
                                                  '192.168.1.10\n')
        result = get_local_ip()
        self.assertEqual(result, '192.168.1.10')

    @patch('subprocess.run')
    def test_invalid_command(self, mock_run):
        # Simulate a case where subprocess.run raises a CalledProcessError
        mock_run.side_effect = subprocess.CalledProcessError(1, 'ipconfig')
        result = get_local_ip()
        self.assertIsNone(result)

    @patch('subprocess.run')
    def test_unexpected_error(self, mock_run):
        # Simulate an unexpected error
        mock_run.side_effect = Exception("Unexpected error")
        result = get_local_ip()
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()