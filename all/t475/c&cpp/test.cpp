TEST_CASE("TestSafeFormat", "[safe_format]") {
    SECTION("test_full_replacement") {
        // Test with all placeholders having corresponding values.
        std::string template_str = "Hello, {name}! Welcome to {place}.";
        std::unordered_map<std::string, std::string> kwargs = {
            {"name", "Alice"},
            {"place", "Wonderland"}
        };
        std::string result = safe_format(template_str, kwargs);
        std::string expected = "Hello, Alice! Welcome to Wonderland.";
        REQUIRE(result == expected);
    }

    SECTION("test_partial_replacement") {
        // Test with some placeholders missing corresponding values.
        std::string template_str = "Hello, {name}! Welcome to {place}.";
        std::unordered_map<std::string, std::string> kwargs = {
            {"name", "Alice"}
        };
        std::string result = safe_format(template_str, kwargs);
        std::string expected = "Hello, Alice! Welcome to {place}.";
        REQUIRE(result == expected);
    }

    SECTION("test_no_replacement") {
        // Test when no placeholders are provided.
        std::string template_str = "Hello, world!";
        std::unordered_map<std::string, std::string> kwargs;
        std::string result = safe_format(template_str, kwargs);
        std::string expected = "Hello, world!";
        REQUIRE(result == expected);
    }

    SECTION("test_missing_placeholder") {
        // Test with a placeholder that has no corresponding value.
        std::string template_str = "My name is {name}, and I live in {city}.";
        std::unordered_map<std::string, std::string> kwargs = {
            {"name", "Alice"}
        };
        std::string result = safe_format(template_str, kwargs);
        std::string expected = "My name is Alice, and I live in {city}.";
        REQUIRE(result == expected);
    }

    SECTION("test_numeric_values") {
        // Test with numeric values as replacements.
        std::string template_str = "Your score is {score} out of {total}.";
        std::unordered_map<std::string, std::string> kwargs = {
            {"score", "85"},
            {"total", "100"}
        };
        std::string result = safe_format(template_str, kwargs);
        std::string expected = "Your score is 85 out of 100.";
        REQUIRE(result == expected);
    }
}