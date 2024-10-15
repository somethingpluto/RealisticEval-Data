TEST_CASE("arabicToEnglishNumbers") {
    SECTION("should convert Arabic numerals to English numerals") {
        std::string input = "١٢٣٤٥٦٧٨٩٠";
        std::string expectedOutput = "1234567890";
        REQUIRE(arabicToEnglishNumbers(input) == expectedOutput);
    }

    SECTION("should return the same string if there are no Arabic numerals") {
        std::string input = "Hello, World!";
        std::string expectedOutput = "Hello, World!";
        REQUIRE(arabicToEnglishNumbers(input) == expectedOutput);
    }

    SECTION("should handle a mix of Arabic numerals and English characters") {
        std::string input = "رقم ١٢٣ هو المثال";
        std::string expectedOutput = "رقم 123 هو المثال";
        REQUIRE(arabicToEnglishNumbers(input) == expectedOutput);
    }

    SECTION("should handle empty string") {
        std::string input = "";
        std::string expectedOutput = "";
        REQUIRE(arabicToEnglishNumbers(input) == expectedOutput);
    }

    SECTION("should handle a string with mixed Arabic and English numerals") {
        std::string input = "The number is ٣٥٦ and 789.";
        std::string expectedOutput = "The number is 356 and 789.";
        REQUIRE(arabicToEnglishNumbers(input) == expectedOutput);
    }
}