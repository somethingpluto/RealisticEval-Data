#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <vector>

std::string getRelativeTime(const std::chrono::system_clock::time_point& messageDate) {
    auto now = std::chrono::system_clock::now();
    auto timeDifference = std::chrono::duration_cast<std::chrono::milliseconds>(now - messageDate).count();

    const long long oneDay = 1000 * 60 * 60 * 24; // milliseconds in one day
    long long daysDifference = timeDifference / oneDay;

    // Check if the message was created today
    if (daysDifference == 0) {
        return "Today";
    }
    // Check if the message was created yesterday
    else if (daysDifference == 1) {
        return "Yesterday";
    }
    // Check if the message was created within the past week (not today or yesterday)
    else if (daysDifference < 7) {
        std::vector<std::string> daysOfWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        // Get the day of the week for the message date
        std::time_t messageTimeT = std::chrono::system_clock::to_time_t(messageDate);
        std::tm* messageTm = std::localtime(&messageTimeT);
        return daysOfWeek[messageTm->tm_wday];
    }
    // If the message was created earlier than one week ago
    else {
        // Format the date to a readable string (e.g., "MM/DD/YYYY")
        std::time_t messageTimeT = std::chrono::system_clock::to_time_t(messageDate);
        std::tm* messageTm = std::localtime(&messageTimeT);

        std::ostringstream oss;
        oss << std::put_time(messageTm, "%m/%d/%Y");
        return oss.str();
    }
}