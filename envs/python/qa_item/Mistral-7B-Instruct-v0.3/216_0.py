import ipaddress
import subprocess

def get_local_ip(interface: str = 'wlan0') -> str:
    try:
        result = subprocess.run(['ip', 'address','show', interface], stdout=subprocess.PIPE)
        lines = result.stdout.decode().splitlines()
        for line in lines:
            if re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)', line):
                ip_address = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)', line).group(1)
                return ip_address
        return f"No IP found for interface '{interface}'"
    except FileNotFoundError:
        return "ip command not found. Please install iproute2 package."
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