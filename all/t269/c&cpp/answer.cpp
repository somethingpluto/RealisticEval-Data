#include <iostream>
#include <string>
#include <boost/asio.hpp>

// Function to check if the given IP address is compliant based on predefined criteria.
bool is_compliant_ip(const std::string& ip) {
    try {
        // Convert the input string to an IP address object
        boost::asio::ip::address ip_obj = boost::asio::ip::make_address(ip);

        // Check compliance criteria: for example, whether the IP is private
        // Note: In Boost.Asio, there is no direct equivalent to `is_private` from Python's ipaddress,
        // so we need to check if the IP falls within private ranges manually.
        std::string ip_str = ip_obj.to_string();
        // Define private IP ranges
        bool is_private = false;

        // IPv4 private ranges
        if (ip_obj.is_v4()) {
            is_private = (ip_str.find("10.") == 0 ||
                          (ip_str.find("172.") == 0 && ip_str.find(".16.") != std::string::npos && ip_str.find(".31.") != std::string::npos) ||
                          ip_str.find("192.168.") == 0);
        }

        // IPv6 private ranges (limited to commonly used ones)
        if (ip_obj.is_v6()) {
            is_private = (ip_str.find("fd") == 0 || ip_str.find("fe80:") == 0);
        }

        return is_private;
    } catch (const std::exception& e) {
        // If the input is not a valid IP address, it cannot be compliant
        return false;
    }
}