#include <iostream>
#include <vector>
#include <string>

struct DictEntry {
    std::string key;
    std::vector<int> values;
};

std::vector<DictEntry> dictOfListsToListOfDicts(const std::vector<DictEntry>& dictOfLists) {
    std::vector<DictEntry> result;

    for (const auto& entry : dictOfLists) {
        DictEntry newEntry;
        newEntry.key = entry.key;
        newEntry.values = entry.values;

        result.push_back(newEntry);
    }

    return result;
}