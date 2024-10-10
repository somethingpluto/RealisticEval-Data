#include <vector>
#include <string>
#include <unordered_set>

std::vector<std::string> findDuplicateIps(std::vector<std::string>& ipList, std::vector<std::string>& ignoreList) {
    std::unordered_set<std::string> ipSet;
    std::unordered_set<std::string> ignoreSet(ignoreList.begin(), ignoreList.end());
    std::vector<std::string> duplicates;

    for(const auto &ip : ipList) {
        if(!ignoreSet.count(ip)) {
            if(ipSet.count(ip)) {
                duplicates.push_back(ip);
            } else {
                ipSet.insert(ip);
            }
        }
    }

    return duplicates;
}