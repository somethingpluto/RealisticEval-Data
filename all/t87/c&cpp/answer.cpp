#include <iostream>
#include <iomanip>
#include <ctime>
#include <sstream>

std::string timestamp_to_readable_date(long long unixTimestamp) {
    std::time_t rawTime = unixTimestamp;
    std::tm* timeInfo = std::localtime(&rawTime);
    std::ostringstream oss;
    oss << std::put_time(timeInfo, "%b %d, %H:%M");
    std::string formattedDate = oss.str();
    int hour = timeInfo->tm_hour;
    int minute = timeInfo->tm_min;

    std::string amPm = (hour >= 12) ? "PM" : "AM";
    if (hour == 0) {
        hour = 12; // Midnight case (00:00)
    } else if (hour > 12) {
        hour -= 12; // Convert PM hour to 12-hour format
    }
    std::ostringstream finalOutput;
    finalOutput << std::put_time(timeInfo, "%b %d, ") << hour << ":"
                << std::setfill('0') << std::setw(2) << minute;
    if (amPm == "AM" || amPm == "PM") {
        finalOutput << " " << amPm;
    }
    return finalOutput.str();
}
