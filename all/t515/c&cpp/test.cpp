TEST_CASE("TestFormatDateString", "[format_date_string]") {
    SECTION("test_valid_date_conversion") {
        const std::string date_str = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)";
        const std::string expected_date = "2023-09-28_14:45:00";
        REQUIRE(format_date_string(date_str) == expected_date);
    }

    SECTION("test_invalid_date_format") {
        const std::string date_str = "Invalid date format";
        REQUIRE(format_date_string(date_str).empty());
    }

    SECTION("test_missing_components") {
        const std::string date_str = "Fri, 28 Sep 2023 14:45:00 +0000";
        REQUIRE(format_date_string(date_str).empty());
    }

    SECTION("test_edge_case_date") {
        const std::string date_str = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        const std::string expected_date = "2024-02-29_14:45:00";
        REQUIRE(format_date_string(date_str) == expected_date);
    }
}