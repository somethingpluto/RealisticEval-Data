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
    def test_no_ip_found(self, mock_run):
        # Configure the mock to simulate no IP found on the interface
        mock_run.return_value = MagicMock(stdout="3: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP>", check=True)
        with self.assertRaises(RuntimeError) as context:
            get_local_ip('wlan0')
        self.assertIn("No local IP found", str(context.exception))

    @patch('subprocess.run')
    def test_command_failure(self, mock_run):
        # Simulate a subprocess failure
        mock_run.side_effect = subprocess.CalledProcessError(1, ['ip', 'addr', 'show', 'wlan0'])
        with self.assertRaises(RuntimeError) as context:
            get_local_ip('wlan0')
        self.assertIn("Failed to retrieve IP address", str(context.exception))

    @patch('subprocess.run')
    def test_different_interface(self, mock_run):
        # Configure the mock for a different interface
        mock_run.return_value = MagicMock(
            stdout="3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n    inet 10.0.0.1/24", check=True)
        ip = get_local_ip('eth0')
        self.assertEqual(ip, '10.0.0.1')

import re
import subprocess

def get_local_ip(interface: str = 'wlan0') -> str:
    """
    Retrieve the local IP address from the specified network interface.

    Args:
    interface (str): The network interface to query. Default is 'wlan0'.

    Returns:
    str: The local IP address, or a message indicating no IP was found.

    Raises:
    RuntimeError: If the subprocess encounters an error or if no suitable IP is found.
    """
    try:
        # Execute the command to get the IP addresses from the specified interface
        result = subprocess.run(['ip', 'addr', 'show', interface],
                                capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle errors from the subprocess command
        raise RuntimeError(f"Failed to retrieve IP address: {str(e)}")

    # Regular expression to match IPv4 addresses, excluding the loopback address
    ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)/\d+')

    # Search for IP addresses in the command output
    ips = ip_pattern.findall(result.stdout)

    # Return the first valid IP found, or raise an error if no IP is found
    if ips:
        return ips[0]
    else:
        raise RuntimeError("No local IP found")