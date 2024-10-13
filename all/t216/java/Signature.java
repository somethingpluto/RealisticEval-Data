/**
 * Gets the IPv4 address of the local computer on a specific network interface, such as wlan0,
 * which is usually a wireless network interface.
 *
 * @param interfaceName The network interface to query. Default is 'wlan0'.
 * @return The local IP address, or a message indicating no IP was found.
 * @throws RuntimeException If the process execution encounters an error or if no suitable IP is found.
 */
public static String getLocalIp(String interfaceName) {}