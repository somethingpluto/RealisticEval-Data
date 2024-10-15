TEST_CASE("getLineNumber") {
    SECTION("returns 1 for the first character") {
        REQUIRE(getLineNumber("Line 1\nLine 2\nLine 3", 0) == 1);
    }

    SECTION("returns 1 for the last character of the first line") {
        REQUIRE(getLineNumber("Line 1\nLine 2\nLine 3", 5) == 1);
    }

    SECTION("returns 3 for the last character of the third line") {
        REQUIRE(getLineNumber("Line 1\nLine 2\nLine 3", 18) == 3);
    }

    SECTION("returns 1 for a single line string") {
        REQUIRE(getLineNumber("Single line string", 0) == 1);
    }

    SECTION("returns 3 for an index within a multiline string with trailing newlines") {
        REQUIRE(getLineNumber("Line 1\nLine 2\nLine 3\n\n", 15) == 3);
    }
}