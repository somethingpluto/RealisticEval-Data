/*
    gets the IPv4 address of the local computer on a specific network interface, such as wlan0, which is usually a wireless network interface
    Args:
        interface (const std::string&): The network interface to query. Default is "wlan0".

    Returns:
        std::string: The local IP address, or a message indicating no IP was found.
    */
std::string getLocalIP(const std::string& interface = "wlan0") {}
    