#include <vector>
#include <string>

std::string boolArrayToBinaryString(const std::vector<bool>& boolArray) {
    std::string binaryString;
    for (bool b : boolArray) {
        binaryString += (b ? '1' : '0');
    }
    return binaryString;
}