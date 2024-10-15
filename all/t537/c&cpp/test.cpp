std::string getTime() {
    std::time_t now = std::time(nullptr);
    std::tm *localTime = std::localtime(&now);
    std::ostringstream oss;
    oss << std::put_time(localTime, "%I:%M %p");
    return oss.str();
}

TEST_CASE("getTime") {
    // Mocking function to set a specific time
    auto mockDate = [](const std::string& dateString) {
        std::tm tm = {};
        std::istringstream ss(dateString);
        ss >> std::get_time(&tm, "%Y-%m-%dT%H:%M:%S");
        std::time_t mockTime = std::mktime(&tm);
        std::tm *localTime = std::localtime(&mockTime);
        return localTime;
    };

    SECTION("should return a string") {
        std::tm* mockTime = mockDate("2024-10-01T10:30:00");
        std::string result = getTime(); // Adjust this to use mocked time in your actual implementation
        REQUIRE(result.length() > 0);
    }

    SECTION("should return a formatted time string including AM/PM") {
        std::tm* mockTime = mockDate("2024-10-01T15:45:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(std::regex_match(result, std::regex("^\\d{1,2}:\\d{2} (AM|PM)$")));
    }

    SECTION("should return the correct time during AM hours") {
        std::tm* mockTime = mockDate("2024-10-01T08:15:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(result == "8:15 AM");
    }

    SECTION("should return the correct time during PM hours") {
        std::tm* mockTime = mockDate("2024-10-01T17:20:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(result == "5:20 PM");
    }

    SECTION("should return '12:00 AM' at midnight") {
        std::tm* mockTime = mockDate("2024-10-01T00:00:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(result == "12:00 AM");
    }

    SECTION("should return '12:00 PM' at noon") {
        std::tm* mockTime = mockDate("2024-10-01T12:00:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(result == "12:00 PM");
    }

    SECTION("should handle single-digit minutes correctly") {
        std::tm* mockTime = mockDate("2024-10-01T09:05:00");
        std::string result = getTime(); // Adjust this to use mocked time
        REQUIRE(result == "9:05 AM");
    }
}