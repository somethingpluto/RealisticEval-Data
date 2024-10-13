#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cstdio>
#include <stdexcept>

std::string get_local_ip(const std::string& interface = "wlan0") {
    std::string command = "ip addr show " + interface;
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        throw std::runtime_error("Failed to execute command");
    }

    std::string result;
    char buffer[128];
    while (!feof(pipe)) {
        if (fgets(buffer, 128, pipe) != nullptr) {
            result += buffer;
        }
    }
    pclose(pipe);

    // Regular expression to match IPv4 addresses, excluding the loopback address
    std::regex ip_pattern("inet ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)/[0-9]+");

    // Search for IP addresses in the command output
    std::smatch match;
    if (std::regex_search(result, match, ip_pattern)) {
        return match[1];
    } else {
        throw std::runtime_error("No local IP found");
    }
}

int main() {
    try {
        std::string local_ip = get_local_ip();
        std::cout << "Local IP: " << local_ip << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}