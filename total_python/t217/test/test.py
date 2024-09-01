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
