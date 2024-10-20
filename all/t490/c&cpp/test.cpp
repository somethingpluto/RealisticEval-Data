TEST_CASE("Test a simple string input", "[format_str]") {
    std::string input_str = "Hello, World!";
    std::string expected_output = "> Hello, World!";
    REQUIRE(format_str(input_str) == expected_output);
}

TEST_CASE("Test a multiline string input", "[format_str]") {
    std::string input_str = "Line 1\nLine 2\nLine 3";
    std::string expected_output = "> Line 1\n> Line 2\n> Line 3";
    REQUIRE(format_str(input_str) == expected_output);
}

TEST_CASE("Test a string with an even number of code block delimiters", "[format_str]") {
    std::string input_str = "Some code:\n```\nprint('Hello')\n```";
    std::string expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```";
    REQUIRE(format_str(input_str) == expected_output);
}

TEST_CASE("Test a string with an odd number of code block delimiters", "[format_str]") {
    std::string input_str = "Some code:\n```\nprint('Hello')";
    std::string expected_output = "> Some code:\n> ```\n> print('Hello')\n> ```";
    REQUIRE(format_str(input_str) == expected_output);
}

TEST_CASE("Test non-string input (e.g., integer) to ensure it's converted", "[format_str]") {
    int input_value = 123;
    std::string expected_output = "> 123";
    REQUIRE(format_str(std::to_string(input_value)) == expected_output);
}