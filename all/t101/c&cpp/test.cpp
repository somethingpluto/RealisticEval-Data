TEST_CASE("isBreakTime Function Tests") {
    SECTION("should return true when current time is exactly at the start time") {
        REQUIRE(isBreakTime("09:00", "10:00", "09:00") == true);
    }

    SECTION("should return true when current time is within the break time range") {
        REQUIRE(isBreakTime("09:00", "10:00", "09:30") == true);
    }

    SECTION("should return false when current time exactly exceeds the end time") {
        REQUIRE(isBreakTime("09:00", "10:00", "10:00") == false);
    }

    SECTION("should return false when current time is before the break time") {
        REQUIRE(isBreakTime("09:00", "10:00", "08:59") == false);
    }

    SECTION("should return false when current time is after the break time") {
        REQUIRE(isBreakTime("09:00", "10:00", "10:01") == false);
    }
}