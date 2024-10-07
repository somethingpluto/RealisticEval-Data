TEST_CASE("Test cases for extractStringFromBraces function") {

    SECTION("Basic extraction") {
        std::string input = "This is a sample text with some data {data: \"value\"} and more text.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "{data: \"value\"}");
    }

    SECTION("No braces") {
        std::string input = "This string has no braces.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "No opening brace found.");
    }

    SECTION("Only opening brace") {
        std::string input = "This string has an opening brace { but no closing brace.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "No closing brace found.");
    }

    SECTION("Only closing brace") {
        std::string input = "This string has a closing brace } but no opening brace.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "No opening brace found.");
    }
    SECTION("Multiple braces") {
        std::string input = "First {first} and second {second} braces.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "{first}");
    }

    SECTION("Empty braces") {
        std::string input = "This string has empty braces {} and some text.";
        std::string result = extractStringFromBraces(input);
        REQUIRE(result == "{}");
    }
}