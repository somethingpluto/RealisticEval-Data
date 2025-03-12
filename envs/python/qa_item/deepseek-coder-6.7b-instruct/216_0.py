import re
import subprocess

def get_local_ip(interface: str = 'wlan0') -> str:
    """
    Gets the IPv4 address of the local computer on a specific network interface.

    Args:
        interface (str): The network interface to query. Default is 'wlan0'.

    Returns:
        str: The local IP address, or a message indicating no IP was found.
    """
    try:
        # Run the 'ip' command to get the network interface details
        result = subprocess.run(['ip', 'addr', 'show', interface], capture_output=True, text=True, check=True)
        
        # Search for the IPv4 address in the output
        ip_match = re.search(r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', result.stdout)
        
        if ip_match:
            return ip_match.group(1)
        else:
            return f"No IP address found for interface {interface}"
    
    except subprocess.CalledProcessError:
        return f"Interface {interface} not found or no IP address assigned"
import unittest
from unittest.mock import patch, MagicMock


class TestGetLocalIp(unittest.TestCase):
    def setUp(self):
        # Sample IP command output for a wlan0 interface
        self.sample_output = "3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000\n" \
                             "    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0\n" \
                             "       valid_lft 86394sec preferred_lft 86394sec\n"

    @patch('subprocess.run')
    def test_successful_ip_retrieval(self, mock_run):
        # Configure the mock to return a successful output
        mock_run.return_value = MagicMock(stdout=self.sample_output, check=True)
        # Test function with wlan0 interface
        ip = get_local_ip('wlan0')
        self.assertEqual(ip, '192.168.1.100')

    @patch('subprocess.run')
    def test_command_failure(self, mock_run):
        # Simulate a subprocess failure
        mock_run.side_effect = subprocess.CalledProcessError(1, ['ip', 'addr', 'show', 'wlan0'])
        self.assertRaises(Exception)
    @patch('subprocess.run')
    def test_different_interface(self, mock_run):
        # Configure the mock for a different interface
        mock_run.return_value = MagicMock(
            stdout="3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n    inet 10.0.0.1/24", check=True)
        ip = get_local_ip('eth0')
        self.assertEqual(ip, '10.0.0.1')
if __name__ == '__main__':
    unittest.main()