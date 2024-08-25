def get_local_ip(interface: str = 'wlan0') -> str:
    """
    gets the IPv4 address of the local computer on a specific network interface, such as wlan0, which is usually a wireless network interface
    Args:
        interface (str): The network interface to query. Default is 'wlan0'.

    Returns:
        str: The local IP address, or a message indicating no IP was found.
    """