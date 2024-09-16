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