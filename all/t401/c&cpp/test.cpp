TEST_CASE("Test find_placeholders function", "[find_placeholders]") {
    SECTION("Test string with multiple placeholders") {
        std::string input_text = "Here are some placeholders: {{ placeholder1 }}, {{ placeholder2 }}, and {{ placeholder3 }}.";
        std::vector<std::string> expected_output = {"placeholder1", "placeholder2", "placeholder3"};
        REQUIRE(find_placeholders(input_text) == expected_output);
    }

    SECTION("Test string with no placeholders") {
        std::string input_text = "This string has no placeholders.";
        std::vector<std::string> expected_output = {};
        REQUIRE(find_placeholders(input_text) == expected_output);
    }

    SECTION("Test string with a single placeholder") {
        std::string input_text = "The only placeholder is {{ singlePlaceholder }}.";
        std::vector<std::string> expected_output = {"singlePlaceholder"};
        REQUIRE(find_placeholders(input_text) == expected_output);
    }

    SECTION("Test string with placeholders that have extra spaces") {
        std::string input_text = "Placeholders with spaces: {{  placeholder_with_spaces  }} and {{ placeholder2 }}.";
        std::vector<std::string> expected_output = {"placeholder_with_spaces", "placeholder2"};
        REQUIRE(find_placeholders(input_text) == expected_output);
    }
}