#include <iostream>
#include <string>
#include <algorithm>

std::pair<std::string, std::string> alignLinesLeft(const std::string& str1, const std::string& str2) {
    size_t maxLength = std::max(str1.length(), str2.length());
    
    // Create new strings with padding
    std::string paddedStr1 = str1;
    std::string paddedStr2 = str2;

    paddedStr1.resize(maxLength);
    paddedStr2.resize(maxLength);

    return {paddedStr1, paddedStr2};
}