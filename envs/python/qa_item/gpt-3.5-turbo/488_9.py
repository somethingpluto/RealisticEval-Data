import subprocess
import re
from typing import Optional

def get_local_ip(interface: str = 'Wi-Fi') -> Optional[str]:
    ipconfig_process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ipconfig_output, _ = ipconfig_process.communicate()

    ip_address_pattern = re.compile(r'IPv4 Address(?:.*: )([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')

    for match in ip_address_pattern.finditer(ipconfig_output):
        if interface in match.group():
            return match.group(1)

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