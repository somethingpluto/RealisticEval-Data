TEST_CASE("timePassed function") {
    SECTION("should correctly calculate time passed from 1 minute ago") {
        long long startTime = 1609459140000; // 1 minute earlier
        REQUIRE(time_passed(startTime) == "1:00");
    }

    SECTION("should handle the boundary of 59 seconds correctly") {
        long long startTime = 1609459194100; // 59 seconds and 900 milliseconds earlier
        REQUIRE(time_passed(startTime) == "0:05");
    }

    SECTION("should return 0:00 when start time is the same as current time") {
        REQUIRE(time_passed(1609459200000) == "0:00");
    }

    SECTION("should handle negative time differences (future start time)") {
        long long startTime = 1609459260000; // 1 minute into the future
        std::string result = time_passed(startTime);
        REQUIRE(result.find('-') != std::string::npos); // Expecting negative output or error handling
    }

    SECTION("should handle very large time differences correctly") {
        long long startTime = 1483228800000; // January 1, 2017, 00:00:00 (4 years difference)
        REQUIRE(time_passed(startTime) == "2103840:00"); // Calculated minutes for 4 years
    }
}