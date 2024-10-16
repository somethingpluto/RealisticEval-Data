TEST_CASE("Test Simple Line Break") {
    std::string input = "Hello<br>World";
    std::string expectedOutput = "Hello\nWorld";
    REQUIRE(convert(input) == expectedOutput);
}

TEST_CASE("Test Strong Tags") {
    std::string input = "This is <strong>important</strong> text.";
    std::string expectedOutput = "This is **important** text.";
    REQUIRE(convert(input) == expectedOutput);
}

TEST_CASE("Test Emphasis Tags") {
    std::string input = "This is <em>emphasized</em> text.";
    std::string expectedOutput = "This is *emphasized* text.";
    REQUIRE(convert(input) == expectedOutput);
}

TEST_CASE("Test Unordered List") {
    std::string input = "<ul><li>Item 1</li><li>Item 2</li></ul>";
    std::string expectedOutput = "* Item 1\n* Item 2";
    REQUIRE(convert(input) == expectedOutput);
}

TEST_CASE("Test Anchor Tags") {
    std::string input = "Check this link: <a href=\"http://example.com\">Example</a>.";
    std::string expectedOutput = "Check this link: [Example](http://example.com).";
    REQUIRE(convert(input) == expectedOutput);
}