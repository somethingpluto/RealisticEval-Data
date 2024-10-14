TEST_CASE("TestFormatTimestampToString", "[format_timestamp_to_string]") {
    SECTION("test_basic_functionality") {
        double timestamp = 1655364000.0; // Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
        std::string expected_date_str = "Thu Jun 16 03:20:00 PM +0800 2022";
        REQUIRE(format_timestamp_to_string(timestamp) == expected_date_str);
    }

    SECTION("test_default_format") {
        double timestamp = 1655364000.0;
        std::string expected_date_str = "Thu Jun 16 03:20:00 PM +0800 2022";
        REQUIRE(format_timestamp_to_string(timestamp) == expected_date_str);
    }

    SECTION("test_custom_format") {
        double timestamp = 1655364000.0;
        std::string custom_format = "%Y-%m-%d %H:%M:%S";
        std::string expected_date_str = "2022-06-16 15:20:00";
        REQUIRE(format_timestamp_to_string(timestamp, custom_format) == expected_date_str);
    }

    SECTION("test_edge_case_boundary_value") {
        double timestamp = 0.0; // Unix epoch start
        std::string expected_date_str = "Thu Jan 01 08:00:00 AM +0800 1970";
        REQUIRE(format_timestamp_to_string(timestamp) == expected_date_str);
    }
}