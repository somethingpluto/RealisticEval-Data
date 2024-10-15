TEST_CASE("getTimeSinceBornUntilNow") {
    // Mocking system time for testing
    std::tm mockTime = {};
    strptime("2024-08-23 15:45:00", "%Y-%m-%d %H:%M:%S", &mockTime);
    time_t systemTime = mktime(&mockTime);
    std::tm* oldTime = localtime(&systemTime);

    SECTION("should return the correct difference for a typical birth date") {
        std::tm birthDate = {};
        strptime("1990-05-15 10:30:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{34, 3, 8, 5, 15});
    }

    SECTION("should return the correct difference for a recent birth date") {
        std::tm birthDate = {};
        strptime("2024-08-20 12:00:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{0, 0, 3, 3, 45});
    }

    SECTION("should handle edge cases at the end of the year") {
        std::tm birthDate = {};
        strptime("2023-12-31 23:59:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{0, 7, 22, 15, 46});
    }

    SECTION("should handle birthdays earlier in the current month") {
        std::tm birthDate = {};
        strptime("2024-08-01 00:00:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{0, 0, 22, 15, 45});
    }

    SECTION("should handle birthdays later in the current year before the current month") {
        std::tm birthDate = {};
        strptime("2024-01-01 01:00:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{0, 7, 22, 14, 45});
    }

    SECTION("should handle birthdays in the previous month of the same year") {
        std::tm birthDate = {};
        strptime("2024-07-30 10:00:00", "%Y-%m-%d %H:%M:%S", &birthDate);
        auto result = getTimeSinceBornUntilNow(birthDate);
        REQUIRE(result == std::array<int, 5>{0, 0, 24, 5, 45});
    }
}