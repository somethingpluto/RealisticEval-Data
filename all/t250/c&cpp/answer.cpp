#include <iostream>
#include <unordered_map>
#include <vector>

std::unordered_map<int, std::vector<int>> invertDictionary(const std::unordered_map<int, int>& originalDict) {
    std::unordered_map<int, std::vector<int>> invertedDict;

    for (const auto& pair : originalDict) {
        invertedDict[pair.second].push_back(pair.first);
    }

    return invertedDict;
}