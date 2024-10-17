#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <windows.h>
#include <Shlwapi.h>

#pragma comment(lib, "Shlwapi.lib")

std::optional<std::string> get_local_ip(const std::string& interface = "Wi-Fi") {
    /**
     * Retrieve the local IP address of the specified network interface on Windows.
     *
     * Args:
     * interface (std::string): The name of the network interface to check (default is "Wi-Fi").
     *
     * Returns:
     * std::optional<std::string>: The local IP address if found, otherwise std::nullopt.
     */
    try {
        // Execute the 'ipconfig' command to get addresses for the specified interface
        STARTUPINFOA si;
        PROCESS_INFORMATION pi;

        ZeroMemory(&si, sizeof(si));
        si.cb = sizeof(si);
        ZeroMemory(&pi, sizeof(pi));

        // Start the child process
        if (!CreateProcessA(NULL, const_cast<char*>("ipconfig"), NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
            std::cerr << "Error executing command." << std::endl;
            return std::nullopt;
        }

        // Read the output of the command
        HANDLE hStdout = pi.hProcess;
        char buffer[256];
        DWORD bytesRead;
        std::string output;

        while (ReadFile(hStdout, buffer, sizeof(buffer) - 1, &bytesRead, NULL) && bytesRead > 0) {
            buffer[bytesRead] = '\0';
            output += buffer;
        }

        // Close process handles
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);

        // Regular expression to match IPv4 addresses
        std::regex ip_pattern(R"((\d+\.\d+\.\d+\.\d+))");

        // Search for IP addresses in the command output
        std::smatch matches;
        std::string::const_iterator searchStart(output.cbegin());
        while (std::regex_search(searchStart, output.cend(), matches, ip_pattern)) {
            std::string ip = matches[0];
            if (PathIsLocalMachineA(ip.c_str())) {
                return ip;
            }
            searchStart = matches.suffix().first;
        }

        return std::nullopt;  // Return std::nullopt if no suitable IP is found

    } catch (const std::exception& e) {
        std::cerr << "An unexpected error occurred: " << e.what() << std::endl;
        return std::nullopt;
    }
}
