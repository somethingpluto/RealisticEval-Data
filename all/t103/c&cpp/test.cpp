TEST_CASE("truncateStringWithReplacement") {
    SECTION("should return the original string if it is shorter than maxLength") {
        REQUIRE(truncateStringWithReplacement("Hello World", 20) == "Hello World");
    }

    SECTION("should truncate the string and replace the excess with ellipsis when longer than maxLength") {
        REQUIRE(truncateStringWithReplacement("This is a long string that needs to be truncated.", 20) == "This is a long str...");
    }

    SECTION("should truncate the string at maxLength and add ellipsis") {
        REQUIRE(truncateStringWithReplacement("Short string", 10) == "Short str...");
    }

    SECTION("should handle empty string correctly") {
        REQUIRE(truncateStringWithReplacement("", 10) == "");
    }

    SECTION("should return the original string when maxLength is equal to string length") {
        REQUIRE(truncateStringWithReplacement("Exact length", 12) == "Exact length");
    }

    SECTION("should replace excess part with ellipsis in a string with special characters") {
        REQUIRE(truncateStringWithReplacement("This string has special characters: !@#$%^&*()", 30) == "This string has special c...");
    }

    SECTION("should return ellipsis only when the maxLength is 0") {
        REQUIRE(truncateStringWithReplacement("Hello, world!", 0) == "...");
    }
}