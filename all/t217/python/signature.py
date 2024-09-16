import socket

def get_local_ip():
    """
    Get the local IP address of the current machine by creating a temporary socket.
    It tries to connect to a remote address, but no actual connection is made.

    Returns:
    - str: The local IP address or an error message if unable to determine.
    """