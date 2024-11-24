TEST_CASE("Test clean_dictionary function", "[clean_dictionary]") {
    SECTION("Test a dictionary with valid strings") {
        std::map<std::string, std::string> input_dict = {
            {"key1", "valid string"},
            {"key2", "another valid string"}
        };
        std::map<std::string, std::string> expected_output = {
            {"key1", "valid string"},
            {"key2", "another valid string"}
        };
        REQUIRE(clean_dictionary(input_dict) == expected_output);
    }

    SECTION("Test a dictionary with None and NaN values") {
        std::map<std::string, std::string> input_dict = {
            {"key1", ""},
            {"key3", "valid string"}
        };
        std::map<std::string, std::string> expected_output = {
            {"key3", "valid string"}
        };
        REQUIRE(clean_dictionary(input_dict) == expected_output);
    }

    SECTION("Test a dictionary with whitespace strings") {
        std::map<std::string, std::string> input_dict = {
            {"key1", "   "},
            {"key2", ""},
            {"key3", "valid"}
        };
        std::map<std::string, std::string> expected_output = {
            {"key3", "valid"}
        };
        REQUIRE(clean_dictionary(input_dict) == expected_output);
    }

    SECTION("Test an empty dictionary") {
        std::map<std::string, std::string> input_dict = {};
        std::map<std::string, std::string> expected_output = {};
        REQUIRE(clean_dictionary(input_dict) == expected_output);
    }
}