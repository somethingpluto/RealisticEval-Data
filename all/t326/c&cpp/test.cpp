TEST_CASE("calculateTimeDifference") {
    SECTION("should return correct time difference for a date in the past") {
        auto pastDate = std::chrono::system_clock::now() - std::chrono::hours(3 * 24 + 5 / 60);
        std::time_t pastTime = std::chrono::system_clock::to_time_t(pastDate);
        std::tm* tmPast = std::localtime(&pastTime);
        char buffer[20];
        std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", tmPast);
        
        TimeDifference result = calculateTimeDifference(buffer);
        REQUIRE(result.days == 3);
        REQUIRE(result.hours == 0);
        REQUIRE(result.minutes == 5);
    }

    SECTION("should return correct time difference for a date that is exactly now") {
        auto now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
        std::tm* tmNow = std::localtime(&now);
        char buffer[20];
        std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", tmNow);

        TimeDifference result = calculateTimeDifference(buffer);
        REQUIRE(result.days == 0);
        REQUIRE(result.hours == 0);
        REQUIRE(result.minutes == 0);
    }

    SECTION("should return correct time difference for a date just seconds ago") {
        auto justNow = std::chrono::system_clock::now() - std::chrono::seconds(45);
        std::time_t justNowTime = std::chrono::system_clock::to_time_t(justNow);
        std::tm* tmJustNow = std::localtime(&justNowTime);
        char buffer[20];
        std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", tmJustNow);
        
        TimeDifference result = calculateTimeDifference(buffer);
        REQUIRE(result.days == 0);
        REQUIRE(result.hours == 0);
        REQUIRE(result.minutes == 0);
    }

    SECTION("should return correct time difference for a date with only hours difference") {
        auto hoursAgo = std::chrono::system_clock::now() - std::chrono::hours(7);
        std::time_t hoursAgoTime = std::chrono::system_clock::to_time_t(hoursAgo);
        std::tm* tmHoursAgo = std::localtime(&hoursAgoTime);
        char buffer[20];
        std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", tmHoursAgo);

        TimeDifference result = calculateTimeDifference(buffer);
        REQUIRE(result.days == 0);
        REQUIRE(result.hours == 7);
        REQUIRE(result.minutes == 0);
    }

    SECTION("should return correct time difference for a date with hours and minutes difference") {
        auto hoursAndMinutesAgo = std::chrono::system_clock::now() - std::chrono::hours(24) - std::chrono::minutes(3);
        std::time_t hoursAndMinutesAgoTime = std::chrono::system_clock::to_time_t(hoursAndMinutesAgo);
        std::tm* tmHoursAndMinutesAgo = std::localtime(&hoursAndMinutesAgoTime);
        char buffer[20];
        std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", tmHoursAndMinutesAgo);

        TimeDifference result = calculateTimeDifference(buffer);
        REQUIRE(result.days == 1);
        REQUIRE(result.hours == 0);
        REQUIRE(result.minutes == 3);
    }
}