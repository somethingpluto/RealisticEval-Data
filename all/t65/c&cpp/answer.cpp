#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <string>

// Function to find duplicate IPs in the given IP list excluding specified IPs to ignore.
std::vector<std::string> findDuplicateIPs(const std::vector<std::string>& ipList, const std::vector<std::string>& ignoreList) {
    // Convert ignoreList to an unordered_set for faster lookups
    std::unordered_set<std::string> ignoreSet(ignoreList.begin(), ignoreList.end());

    // Unordered map to count occurrences of each IP
    std::unordered_map<std::string, int> ipCount;

    // Count occurrences of each IP, excluding ignored IPs
    for (const auto& ip : ipList) {
        if (ignoreSet.find(ip) == ignoreSet.end()) {
            if (ipCount.find(ip) != ipCount.end()) {
                ipCount[ip]++;
            } else {
                ipCount[ip] = 1;
            }
        }
    }

    // Collect duplicate IPs
    std::vector<std::string> duplicates;
    for (const auto& entry : ipCount) {
        if (entry.second > 1) {
            duplicates.push_back(entry.first);
        }
    }

    return duplicates;
}

int main() {
    // Example usage
    std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.2", "192.168.1.1", "10.0.0.1", "10.0.0.1"};
    std::vector<std::string> ignoreList = {"192.168.1.2"};

    std::vector<std::string> duplicates = findDuplicateIPs(ipList, ignoreList);

    // Print the duplicates
    for (const auto& ip : duplicates) {
        std::cout << ip << std::endl;
    }

    return 0;
}