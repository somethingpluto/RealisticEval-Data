/**
 * @brief Retrieve the local IP address of the specified network interface on Windows.
 *
 * @param interface The name of the network interface to check (default is "Wi-Fi").
 * @return The local IP address if found, otherwise std::nullopt.
 */
using OptionalString = std::optional<std::string>;
OptionalString get_local_ip(const std::string& interface = "Wi-Fi") {}