#include <iostream>
#include <vector>
#include <array>

int calculate_total_seconds(const std::vector<int>& time) {
    const int SECONDS_PER_DAY = 86400;
    const int SECONDS_PER_HOUR = 3600;
    const int SECONDS_PER_MINUTE = 60;

    // Unpacking the time with defaults
    int days = 0, hours = 0, minutes = 0, seconds = 0;
    if (time.size() > 0) days = time[0];
    if (time.size() > 1) hours = time[1];
    if (time.size() > 2) minutes = time[2];
    if (time.size() > 3) seconds = time[3];

    int total_seconds = (
        days * SECONDS_PER_DAY +
        hours * SECONDS_PER_HOUR +
        minutes * SECONDS_PER_MINUTE +
        seconds
    );

    return total_seconds;
}