TEST_CASE("countLetters", "[countLetters]") {
    SECTION("should return 10 for the string 'Hello, World!'") {
        REQUIRE(countLetters("Hello, World!") == 10);
    }

    SECTION("should return 0 for a string with no letters '12345'") {
        REQUIRE(countLetters("12345") == 0);
    }

    SECTION("should return 6 for the string 'abc 123 xyz!'") {
        REQUIRE(countLetters("abc 123 xyz!") == 6);
    }

    SECTION("should return 0 for an empty string") {
        REQUIRE(countLetters("") == 0);
    }

    SECTION("should return 3 for the string 'A1B2C3!@#'") {
        REQUIRE(countLetters("A1B2C3!@#") == 3);
    }

    SECTION("should return 5 for a string with mixed case 'AbCdE'") {
        REQUIRE(countLetters("AbCdE") == 5);
    }

    SECTION("should return 5 for a string with special characters 'Hello@2024!'") {
        REQUIRE(countLetters("Hello@2024!") == 5);
    }
}