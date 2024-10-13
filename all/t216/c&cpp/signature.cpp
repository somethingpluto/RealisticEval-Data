/**
 * Gets the IPv4 address of the local computer on a specific network interface,
 * such as wlan0, which is usually a wireless network interface.
 *
 * @param interface The network interface to query. Default is 'wlan0'.
 * @return The local IP address, or a message indicating no IP was found.
 */
std::string get_local_ip(const std::string& interface = "wlan0") {}