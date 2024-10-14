TEST_CASE("Test date_range_string function") {
    SECTION("Test dates within the same month") {
        std::string result = date_range_string("2023-08-01", "2023-08-15");
        REQUIRE(result == "August 1 to 15, 2023");
    }

    SECTION("Test dates within the same month (start and end)") {
        std::string result = date_range_string("2023-08-01", "2023-08-31");
        REQUIRE(result == "August 1 to 31, 2023");
    }

    SECTION("Test dates across different months within the same year") {
        std::string result = date_range_string("2023-08-30", "2023-09-05");
        REQUIRE(result == "August 30, 2023 to September 5, 2023");
    }

    SECTION("Test dates across different years") {
        std::string result = date_range_string("2023-12-30", "2024-01-02");
        REQUIRE(result == "December 30, 2023 to January 2, 2024");
    }
}