#include <string>
#include <unordered_map>
#include <algorithm>

std::string arabicToEnglishNumbers(const std::string& str) {
    std::unordered_map<char, char> arabicNums = {
        {'٠', '0'}, {'١', '1'}, {'٢', '2'}, {'٣', '3'}, {'٤', '4'},
        {'٥', '5'}, {'٦', '6'}, {'٧', '7'}, {'٨', '8'}, {'٩', '9'}
    };

    std::string result;
    for (char ch : str) {
        result += arabicNums.count(ch) ? arabicNums[ch] : ch;
    }
    return result;
}