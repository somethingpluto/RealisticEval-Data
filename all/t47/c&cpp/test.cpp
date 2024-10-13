TEST_CASE("Test find_nth_weekday_of_specific_year", "[find_nth_weekday_of_specific_year]") {
    SECTION("Regular occurrence") {
        // Test for the 2nd Monday of May 2023
        auto result = find_nth_weekday_of_specific_year(2023, 5, 2, 0);  // Monday is 0
        auto expected = std::chrono::sys_days{std::chrono::year_month_day{std::chrono::year{2023}, std::chrono::month{5}, std::chrono::day{8}}};
        REQUIRE(result == expected);
    }

    SECTION("Last occurrence") {
        // Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        auto result = find_nth_weekday_of_specific_year(2023, 5, 5, 0);  // Monday is 0
        auto expected = std::chrono::sys_days{std::chrono::year_month_day{std::chrono::year{2023}, std::chrono::month{5}, std::chrono::day{29}}};
        REQUIRE(result == expected);
    }

    SECTION("First day is weekday") {
        // Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        auto result = find_nth_weekday_of_specific_year(2023, 8, 1, 1);  // Tuesday is 1
        auto expected = std::chrono::sys_days{std::chrono::year_month_day{std::chrono::year{2023}, std::chrono::month{8}, std::chrono::day{1}}};
        REQUIRE(result == expected);
    }

    SECTION("Edge year transition") {
        // Test for the 1st Friday of December 2023
        auto result = find_nth_weekday_of_specific_year(2023, 12, 1, 4);  // Friday is 4
        auto expected = std::chrono::sys_days{std::chrono::year_month_day{std::chrono::year{2023}, std::chrono::month{12}, std::chrono::day{1}}};
        REQUIRE(result == expected);
    }
}