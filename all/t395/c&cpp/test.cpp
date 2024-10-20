TEST_CASE("Test sum_calibration_values", "[sum_calibration_values]") {
    SECTION("test_basic_calculations") {
        // Test with a simple input where lines contain at least two digits
        std::vector<std::string> document = {
            "Reading 1234 calibration",
            "Measure 5678 complete",
            "End of data 91011"
        };
        REQUIRE(sum_calibration_values(document) == 163);
    }

    SECTION("test_no_digits") {
        // Test lines with no digits
        std::vector<std::string> document = {
            "No numbers here",
            "Still no numbers"
        };
        REQUIRE(sum_calibration_values(document) == 0);
    }

    SECTION("test_empty_lines") {
        // Test with empty lines or lines with spaces
        std::vector<std::string> document = {
            "",
            "   "
        };
        REQUIRE(sum_calibration_values(document) == 0);
    }

    SECTION("test_mixed_content") {
        // Test with a mixture of valid and invalid lines
        std::vector<std::string> document = {
            "Good line 1524 end",
            "Bad line",
            "Another good line 7681"
        };
        REQUIRE(sum_calibration_values(document) == 85);
    }
}