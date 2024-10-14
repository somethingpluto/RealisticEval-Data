#include <iostream>
#include <chrono>
#include <ctime>
#include <stdexcept>
#include <string>
#include <optional>

// Utility function to get the local timezone
std::optional<std::string> get_local_timezone() {
    // In C++, getting the local timezone name is not straightforward.
    // For simplicity, we assume "localtime" is the local timezone.
    return "localtime";
}

std::string format_datetime_str(double mtime, const std::string& format = "%a %b %d %I:%M:%S %p %z %Y") {
    if (mtime < 0) {
        throw std::invalid_argument("error mtime");
    }

    std::optional<std::string> local_tz = get_local_timezone();
    if (!local_tz.has_value()) {
        // Fallback to UTC if the local timezone is not found
        local_tz = "UTC";
    }

    try {
        // Convert the UNIX timestamp to a time_t value
        std::time_t raw_time = static_cast<std::time_t>(mtime);
        std::tm* ptm;

        // Use local time if the timezone is "localtime", otherwise use UTC
        if (local_tz.value() == "localtime") {
            ptm = std::localtime(&raw_time);
        } else {
            ptm = std::gmtime(&raw_time);
        }

        // Format the datetime string
        char buffer[128];
        if (std::strftime(buffer, sizeof(buffer), format.c_str(), ptm) == 0) {
            throw std::runtime_error("Error formatting the datetime");
        }

        return std::string(buffer);
    } catch (const std::exception& e) {
        // Handle any other unexpected errors
        throw std::invalid_argument("Error formatting the datetime: " + std::string(e.what()));
    }
}
