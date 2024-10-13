TEST_CASE("Test Replace Phone Numbers") {
    SECTION("Basic Number") {
        std::string msg = "Call me at 123-456-7890.";
        std::string expected = "Call me at [PHONE_NUM].";
        REQUIRE(replace_phone_numbers(msg) == expected);
    }

    SECTION("Number with Parentheses") {
        std::string msg = "Our office number is 123 456-7890.";
        std::string expected = "Our office number is [PHONE_NUM].";
        REQUIRE(replace_phone_numbers(msg) == expected);
    }

    SECTION("Number with Dots") {
        std::string msg = "Fax us at 123.456.7890.";
        std::string expected = "Fax us at [PHONE_NUM].";
        REQUIRE(replace_phone_numbers(msg) == expected);
    }

    SECTION("No Phone Number") {
        std::string msg = "Hello, please reply to this email.";
        std::string expected = "Hello, please reply to this email.";
        REQUIRE(replace_phone_numbers(msg) == expected);
    }
}