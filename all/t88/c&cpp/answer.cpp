#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <iostream>

bool is_cron_between2_and4_am(const std::string& cronExpression) {
    // Split the cron expression by spaces
    std::istringstream stream(cronExpression);
    std::string minute, hour, dayOfMonth, month, dayOfWeek;
    
    stream >> minute >> hour >> dayOfMonth >> month >> dayOfWeek;

    // Now, we need to parse the hour field (which is in the 'hour' variable)
    if (hour == "*") {
        return false;  // Wildcard means any hour, hence not specifically between 2 and 4 a.m.
    }

    // Set to store the allowed hours (2, 3, 4)
    std::set<int> allowedHours = {2, 3, 4};
    
    // Check if the hour field is a range or a list
    if (hour.find(",") != std::string::npos) {
        // Split by commas and check each hour
        std::istringstream rangeStream(hour);
        std::string hourPart;
        while (std::getline(rangeStream, hourPart, ',')) {
            int h = std::stoi(hourPart);
            if (allowedHours.find(h) == allowedHours.end()) {
                return false;
            }
        }
        return true;
    }
    else if (hour.find("-") != std::string::npos) {
        // Handle range like "2-4"
        size_t dashPos = hour.find("-");
        int start = std::stoi(hour.substr(0, dashPos));
        int end = std::stoi(hour.substr(dashPos + 1));
        
        // Check if the range is within 2-4
        if (start <= 4 && end >= 2) {
            return true;
        } else {
            return false;
        }
    }
    else {
        // It's a single hour value, just check if it's 2, 3, or 4
        int h = std::stoi(hour);
        return allowedHours.find(h) != allowedHours.end();
    }
}