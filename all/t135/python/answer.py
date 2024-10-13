def is_valid_port_number(port: int) -> bool:
    """Checks if the provided port number is within the valid range of TCP/UDP ports.
    
    Valid TCP/UDP port numbers range from 1 to 65535.

    Args:
        port (int): The port number to verify.

    Returns:
        bool: Returns True if the port number is valid, False otherwise.

    Raises:
        TypeError: If the port number is not an integer.
    """
    if not isinstance(port, int):  # Check if port is an integer
        raise TypeError('The port number must be an integer.')
    
    if port < 1 or port > 65535:  # Check if the port is in the valid range
        return False
    
    return True