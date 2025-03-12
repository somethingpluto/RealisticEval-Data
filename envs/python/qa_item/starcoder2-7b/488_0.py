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
    try:
        # Run the ipconfig command and capture the output
        output = subprocess.check_output(["ipconfig"]).decode()

        # Find the section of the output that corresponds to the specified interface
        interface_section = re.search(f'{interface}.*?:', output, re.DOTALL)

        if interface_section:
            # Find the IP address in the interface section
            ip_address = re.search(r'IPv4 Address.*?: (\d+\.\d+\.\d+\.\d+)', interface_section.group())

            if ip_address:
                return ip_address.group(1)

    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

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