#include <iostream>
#include <string>
#include <iomanip>

std::string formatNumber(double num) {
    if (num >= 1000000) {
        std::ostringstream out;
        out << std::fixed << std::setprecision(1) << (num / 1000000) << "M";
        return out.str();
    } else if (num >= 1000) {
        std::ostringstream out;
        out << std::fixed << std::setprecision(1) << (num / 1000) << "K";
        return out.str();
    } else {
        return std::to_string(num);
    }
}