import subprocess
import re
from typing import Optional

def get_local_ip(interface: str = 'Wi-Fi') -> Optional[str]:
    ip_config_output = subprocess.check_output(['ipconfig']).decode('utf-8')
    ip_config_output_lines = ip_config_output.split('\n')
    
    interface_found = False
    ip_address = None
    
    for line in ip_config_output_lines:
        if interface in line:
            interface_found = True
        if interface_found and 'IPv4 Address' in line:
            ip_address = re.search(r'\d+\.\d+\.\d+\.\d+', line).group(0)
            break
    
    return ip_address
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