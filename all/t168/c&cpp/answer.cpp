#include <iostream>
#include <string>
#include <ctime>
#include <stdexcept>

std::string formatDate(const std::string& dateString) {
    // Convert the dateString to time_t
    struct tm tm = {};
    if (strptime(dateString.c_str(), "%Y-%m-%d %H:%M:%S", &tm) == nullptr) {
        throw std::invalid_argument("Invalid Date");
    }

    time_t inputTime = mktime(&tm);
    time_t currentTime = time(nullptr);

    // Calculate time difference in seconds
    double timeDifference = difftime(currentTime, inputTime);

    // Calculate time differences in seconds, minutes, hours, and days
    int secondsDifference = static_cast<int>(timeDifference);
    int minutesDifference = secondsDifference / 60;
    int hoursDifference = minutesDifference / 60;
    int daysDifference = hoursDifference / 24;

    // Determine and return the appropriate time description
    if (daysDifference > 0) {
        return std::to_string(daysDifference) + " day" + (daysDifference != 1 ? "s" : "") + " ago";
    } else if (hoursDifference > 0) {
        return std::to_string(hoursDifference) + " hour" + (hoursDifference != 1 ? "s" : "") + " ago";
    } else if (minutesDifference > 0) {
        return std::to_string(minutesDifference) + " minute" + (minutesDifference != 1 ? "s" : "") + " ago";
    } else {
        return std::to_string(secondsDifference) + " second" + (secondsDifference != 1 ? "s" : "") + " ago";
    }
}
