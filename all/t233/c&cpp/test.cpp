TEST_CASE("Test removeComments functionality", "[removeComments]") {
    SECTION("Test string with a comment on a single line") {
        std::string input_string = "Hello, world!# This is a comment";
        std::string expected_output = "Hello, world!";
        REQUIRE(remove_comments(input_string) == expected_output);
    }

    SECTION("Test string with no comments") {
        std::string input_string = "Hello, world!\nPython is fun!";
        std::string expected_output = "Hello, world!\nPython is fun!";
        REQUIRE(remove_comments(input_string) == expected_output);
    }

    SECTION("Test an empty string") {
        std::string input_string = "";
        std::string expected_output = "";
        REQUIRE(remove_comments(input_string) == expected_output);
    }

    SECTION("Test string where all lines are comments") {
        std::string input_string = "# comment only line\n#another comment line";
        std::string expected_output = "\n";
        REQUIRE(remove_comments(input_string) == expected_output);
    }
}