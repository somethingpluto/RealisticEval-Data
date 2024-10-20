TEST_CASE("TestCleanPattern", "[clean_pattern]") {
    const std::string pattern = R"((\d+\.?\d*) kg)";  // Regex pattern to match weight in kg

    SECTION("test_valid_integer_weight") {
        std::string input_string = "The weight is 25 kg";
        std::string result = clean_pattern(input_string, pattern);
        REQUIRE(result == "25.0");
    }

    SECTION("test_valid_float_weight") {
        std::string input_string = "Weight measured at 15.75 kg";
        std::string result = clean_pattern(input_string, pattern);
        REQUIRE(result == "15.75");
    }

    SECTION("test_no_weight_found") {
        std::string input_string = "No weight provided.";
        std::string result = clean_pattern(input_string, pattern);
        REQUIRE(result.empty());
    }

    SECTION("test_invalid_float_conversion") {
        std::string input_string = "The weight is thirty kg";
        std::string result = clean_pattern(input_string, pattern);
        REQUIRE(result.empty());
    }

    SECTION("test_weight_with_extra_text") {
        std::string input_string = "The total weight is 45.3 kg as per the last measurement.";
        std::string result = clean_pattern(input_string, pattern);
        REQUIRE(result == "45.3");
    }
}