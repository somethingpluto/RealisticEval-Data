TEST_CASE("Test extract_outermost_brackets") {
    SECTION("test_single_parentheses") {
        CHECK(extract_outermost_brackets("Text (example) more text") == "example");
    }

    SECTION("test_nested_brackets") {
        CHECK(extract_outermost_brackets("Text {with some {nested} brackets}") == "with some {nested} brackets");
    }

    SECTION("test_square_brackets") {
        CHECK(extract_outermost_brackets("Text [with [nested] brackets] and more text") == "with [nested] brackets");
    }

    SECTION("test_mixed_bracket_types") {
        CHECK(extract_outermost_brackets("Mixed (types {of brackets [in use]})") == "types {of brackets [in use]}");
    }

    SECTION("test_no_brackets") {
        CHECK(extract_outermost_brackets("No brackets here") == "");
    }
}