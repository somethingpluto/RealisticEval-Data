#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

std::string arabicToEnglishNumbers(const std::string& value) {
    std::unordered_map<char, char> arabicToEnglishMap = {
        {'٠', '0'}, {'١', '1'}, {'٢', '2'}, {'٣', '3'}, {'٤', '4'},
        {'٥', '5'}, {'٦', '6'}, {'٧', '7'}, {'٨', '8'}, {'٩', '9'}
    };

    std::string result;
    result.reserve(value.size()); // Reserve space for efficiency

    for (char ch : value) {
        // Check if the character is in the map, otherwise keep the original
        if (arabicToEnglishMap.find(ch) != arabicToEnglishMap.end()) {
            result += arabicToEnglishMap[ch];
        } else {
            result += ch;
        }
    }

    return result;
}