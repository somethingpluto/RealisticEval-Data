#include <iostream>
#include <chrono>
#include <string>
#include <stdexcept>
#include <iomanip>
#include <sstream>

// Function to parse a date string in 'YYYY-MM-DD' format
std::tm parse_date(const std::string& date_str) {
    std::istringstream ss(date_str);
    std::tm tm = {};
    ss >> std::get_time(&tm, "%Y-%m-%d");
    if (ss.fail()) {
        throw std::invalid_argument("Date must be in 'YYYY-MM-DD' format.");
    }
    return tm;
}

// Function to generate a formatted date range string
std::string date_range_string(const std::string& start_date, const std::string& end_date) {
    try {
        auto start_tm = parse_date(start_date);
        auto end_tm = parse_date(end_date);

        // Convert tm structures to time_points
        std::chrono::system_clock::time_point start_time = std::chrono::system_clock::from_time_t(std::mktime(&start_tm));
        std::chrono::system_clock::time_point end_time = std::chrono::system_clock::from_time_t(std::mktime(&end_tm));

        if (start_time > end_time) {
            throw std::invalid_argument("start_date cannot be after end_date.");
        }

        // Extract month names and day numbers
        std::ostringstream oss_start, oss_end;
        oss_start << std::put_time(&start_tm, "%B %d");
        oss_end << std::put_time(&end_tm, "%B %d");

        std::string start_month, end_month, start_day, end_day, start_year, end_year;
        oss_start >> start_month >> start_day;
        oss_end >> end_month >> end_day;

        start_year = std::to_string(1900 + start_tm.tm_year);
        end_year = std::to_string(1900 + end_tm.tm_year);

        // Format output based on whether dates are within the same month and/or year
        if (start_year != end_year) {
            return fmt::format("{} {}, {} to {} {}, {}", start_month, start_day, start_year, end_month, end_day, end_year);
        } else if (start_month == end_month) {
            return fmt::format("{} {} to {}, {}", start_month, start_day, end_day, start_year);
        } else {
            return fmt::format("{} {} to {} {}, {}", start_month, start_day, end_month, end_day, start_year);
        }
    } catch (const std::exception& e) {
        throw std::invalid_argument(fmt::format("Date must be in 'YYYY-MM-DD' format. {}", e.what()));
    }
}
