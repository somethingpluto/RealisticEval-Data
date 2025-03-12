import re
import subprocess

def get_local_ip(interface: str = 'wlan0') -> str:
    """
    gets the IPv4 address of the local computer on a specific network interface, such as wlan0, which is usually a wireless network interface
    Args:
        interface (str): The network interface to query. Default is 'wlan0'.

    Returns:
        str: The local IP address, or a message indicating no IP was found.
    """

    try:
        ipconfig_process = subprocess.Popen(['ip', 'a', 'show', interface], stdout=subprocess.PIPE)
        ipconfig_output = ipconfig_process.communicate()[0].decode()

        ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', ipconfig_output)
        if ip_match:
            return ip_match.group(1)
        else:
            return "No IP address found for interface: " + interface

    except Exception as e:
        return "Error occurred while fetching IP address: " + str(e)
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