TEST_CASE("JSON extraction tests", "[extract_json]") {

    SECTION("Basic JSON extraction") {
        std::string input = "Here is a JSON: {\"key\": \"value\"} with text.";
        std::string expected = "{\"key\": \"value\"}";
        REQUIRE(token_manager::extract_json(input) == expected);
    }

    SECTION("Nested braces JSON extraction") {
        std::string input = "Prefix {\"outer\": {\"inner\": \"value\"}} Suffix";
        std::string expected = "{\"outer\": {\"inner\": \"value\"}}";
        REQUIRE(token_manager::extract_json(input) == expected);
    }

    SECTION("No braces in input") {
        std::string input = "No JSON here.";
        std::string expected = "";
        REQUIRE(token_manager::extract_json(input) == expected);
    }

    SECTION("Only opening brace") {
        std::string input = "Starts with a brace { but no closing one.";
        std::string expected = "";
        REQUIRE(token_manager::extract_json(input) == expected);
    }

    SECTION("Only closing brace") {
        std::string input = "Ends with a brace } but no opening one.";
        std::string expected = "";
        REQUIRE(token_manager::extract_json(input) == expected);
    }
}