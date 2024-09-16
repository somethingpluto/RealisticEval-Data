"""
Method created by ChatGPT
"""
def get_local_ip_old():
    # Attempt to find the local IP by connecting to a remote address.
    # The chosen address does not need to be reachable or exist.
    try:
        # Create a temporary socket for this purpose
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_socket:
            # Use Google's public DNS server address for the connection attempt.
            # No actual connection is made.
            temp_socket.connect(('8.8.8.8', 80))
            # Get the socket's own address
            local_ip = temp_socket.getsockname()[0]
            return local_ip
    except Exception as e:
        print(f"Error obtaining local IP: {e}")
        return "Unable to determine local IP"