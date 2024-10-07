#include <iostream>
#include <ctime>
#include <iomanip>
#include <sstream>

std::string getCurrentDate() {
    // Get the current time
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);

    // Create a string stream to format the date
    std::stringstream dateStream;
    dateStream << (now->tm_year + 1900) << "-"
               << std::setw(2) << std::setfill('0') << (now->tm_mon + 1) << "-"
               << std::setw(2) << std::setfill('0') << now->tm_mday;

    // Return the formatted date string
    return dateStream.str();
}
