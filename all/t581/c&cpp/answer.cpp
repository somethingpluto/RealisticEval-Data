#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <iomanip>

std::string abbreviateNumber(double number) {
    if (number < 1000) {
        return std::to_string(static_cast<int>(number));
    }

    int tier = static_cast<int>(std::floor(std::log10(number) / 3));
    std::vector<std::string> suffixes = {"", "k", "M", "B", "T"};
    
    double baseNumber = number / std::pow(10, tier * 3);
    std::ostringstream roundedStream;
    roundedStream << std::fixed << std::setprecision(1) << baseNumber;

    return roundedStream.str() + suffixes[tier];
}

int main() {
    double num = 1500;
    std::cout << abbreviateNumber(num) << std::endl; // Output: 1.5k
    return 0;
}