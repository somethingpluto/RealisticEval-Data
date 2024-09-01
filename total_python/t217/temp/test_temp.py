import unittest
from unittest.mock import patch, Mock
import socket

class TestGetLocalIP(unittest.TestCase):

    @patch('socket.socket')
    def test_normal_case(self, mock_socket):
        # Simulate a normal case where the socket successfully retrieves an IP address
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_socket_instance.getsockname.return_value = ('192.168.1.1', 0)

        result = get_local_ip()
        self.assertEqual(result, '192.168.1.1')

    @patch('socket.socket')
    def test_socket_error(self, mock_socket):
        # Simulate a socket error
        mock_socket.side_effect = socket.error("Socket error")

        result = get_local_ip()
        self.assertEqual(result, "Unable to determine local IP")

    @patch('socket.socket')
    def test_general_exception(self, mock_socket):
        # Simulate a general exception
        mock_socket.side_effect = Exception("General error")

        result = get_local_ip()
        self.assertEqual(result, "Unable to determine local IP")

    @patch('socket.socket')
    def test_no_ip_address(self, mock_socket):
        # Simulate a case where no IP address is returned
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_socket_instance.getsockname.return_value = ('', 0)

        result = get_local_ip()
        self.assertEqual(result, '')

    @patch('socket.socket')
    def test_invalid_address(self, mock_socket):
        # Test with an invalid address, simulating an exception in connect()
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_socket_instance.connect.side_effect = socket.error("Invalid address")

        result = get_local_ip()
        self.assertEqual(result, "Unable to determine local IP")

import socket

def get_local_ip():
    """
    Get the local IP address of the current machine by creating a temporary socket.
    It tries to connect to a remote address, but no actual connection is made.

    Returns:
    - str: The local IP address or an error message if unable to determine.
    """
    try:
        # Create a temporary UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_socket:
            # Connect to an external server (Google's public DNS server in this case)
            temp_socket.connect(('8.8.8.8', 80))
            # Retrieve the local IP address from the socket
            local_ip = temp_socket.getsockname()[0]
            return local_ip
    except socket.error as e:
        # Handle socket-related errors
        print(f"Socket error while obtaining local IP: {e}")
        return "Unable to determine local IP"
    except Exception as e:
        # Handle any other exceptions
        print(f"Unexpected error while obtaining local IP: {e}")
        return "Unable to determine local IP"