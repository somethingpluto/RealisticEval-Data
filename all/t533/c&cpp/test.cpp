TEST_CASE("shuffleString") {
    SECTION("should return a string of the same length as the input") {
        std::string input = "abcdef";
        std::string result = shuffleString(input);
        REQUIRE(result.length() == input.length());
    }

    SECTION("should shuffle the characters in the string") {
        std::string input = "hello";
        std::string result = shuffleString(input);
        REQUIRE(result != input); // It should be different most of the time
    }

    SECTION("should return an empty string when given an empty string") {
        std::string input = "";
        std::string result = shuffleString(input);
        REQUIRE(result == ""); // Should return an empty string
    }

    SECTION("should handle a single character string") {
        std::string input = "a";
        std::string result = shuffleString(input);
        REQUIRE(result == "a"); // Should return the same single character
    }

    SECTION("should handle strings with identical characters") {
        std::string input = "aaaaa";
        std::string result = shuffleString(input);
        REQUIRE(result == "aaaaa"); // Should return the same string
    }

    SECTION("should return a shuffled string for longer strings") {
        std::string input = "abcdefghijklmnopqrstuvwxyz";
        std::string result = shuffleString(input);
        REQUIRE(result != input); // It should be different most of the time
        REQUIRE(result.length() == input.length()); // Length should be the same
    }

    SECTION("should return the same string if all characters are the same") {
        std::string input = "111111";
        std::string result = shuffleString(input);
        REQUIRE(result == "111111"); // Should return the same string
    }

    SECTION("should shuffle a string containing special characters") {
        std::string input = "a!@#$%^&*()_+";
        std::string result = shuffleString(input);
        REQUIRE(result.length() == input.length()); // Length should be the same
        REQUIRE(result != input); // It should be different most of the time
    }
}