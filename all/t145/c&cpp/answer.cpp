#include <iostream>
#include <iomanip>
#include <locale>
#include <sstream>

std::string formatCurrency(double value, const std::string& currencyCode, const std::string& locale = "en-US") {
    std::ostringstream oss;
    std::locale loc(locale.c_str());
    oss.imbue(loc);
    
    // Setting up currency formatting
    oss << std::showbase << std::put_money(value * 100) << " " << currencyCode;
    return oss.str();
}