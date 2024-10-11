TEST_CASE("Test gen_timeout_timedelta", "[timedelta]") {
    REQUIRE(gen_timeout_timedelta("1d") == std::chrono::nanoseconds(86400000000000LL));  // 1 day in nanoseconds
    REQUIRE(gen_timeout_timedelta("2h") == std::chrono::nanoseconds(7200000000000LL));   // 2 hours in nanoseconds
    REQUIRE(gen_timeout_timedelta("3m") == std::chrono::nanoseconds(1800000000000LL));   // 3 minutes in nanoseconds
    REQUIRE(gen_timeout_timedelta("4s") == std::chrono::nanoseconds(4000000000LL));      // 4 seconds in nanoseconds
    REQUIRE(gen_timeout_timedelta("500ms") == std::chrono::nanoseconds(500000000LL));     // 500 milliseconds in nanoseconds
    REQUIRE(gen_timeout_timedelta("1d 2h 3m 4s 500ms") == std::chrono::nanoseconds(93964000000000LL));  // Mixed units
}

TEST_CASE("Test invalid input", "[error]") {
    CHECK_THROWS_AS(gen_timeout_timedelta("1z"), std::invalid_argument);  // Invalid unit character
    CHECK_THROWS_WITH(gen_timeout_timedelta(""), std::invalid_argument, "Empty string");  // Empty string
}