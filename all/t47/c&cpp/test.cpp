TEST_CASE("Find Nth Weekday of Specific Year", "[weekday]") {
    // Test Case 1: First Monday of April 2023
    SECTION("First Monday of April 2023") {
        auto result = find_nth_weekday_of_specific_year(2023, 4, 1, 0);
        REQUIRE(result == datetime::date(2023, 4, 3)); // April 3, 2023 is the first Monday
    }

    // Test Case 2: Second Wednesday of May 2023
    SECTION("Second Wednesday of May 2023") {
        auto result = find_nth_weekday_of_specific_year(2023, 5, 2, 2);
        REQUIRE(result == datetime::date(2023, 5, 17)); // May 17, 2023 is the second Wednesday
    }

    // Test Case 3: Third Friday of June 2023
    SECTION("Third Friday of June 2023") {
        auto result = find_nth_weekday_of_specific_year(2023, 6, 3, 4);
        REQUIRE(result == datetime::date(2023, 6, 16)); // June 16, 2023 is the third Friday
    }

    // Test Case 4: Fourth Saturday of July 2023
    SECTION("Fourth Saturday of July 2023") {
        auto result = find_nth_weekday_of_specific_year(2023, 7, 4, 5);
        REQUIRE(result == datetime::date(2023, 7, 29)); // July 29, 2023 is the fourth Saturday
    }

    // Test Case 5: Fifth Sunday of August 2023
    SECTION("Fifth Sunday of August 2023") {
        auto result = find_nth_weekday_of_specific_year(2023, 8, 5, 6);
        REQUIRE(result == datetime::date(2023, 8, 27)); // August 27, 2023 is the fifth Sunday
    }

    // Test Case 6: Non-existent occurrence, should return the last occurrence
    SECTION("Non-existent occurrence, should return the last occurrence") {
        auto result = find_nth_weekday_of_specific_year(2023, 2, 5, 0); // February 2023 has only 4 Mondays
        REQUIRE(result == datetime::date(2023, 2, 20)); // Last Monday in February 2023
    }
}