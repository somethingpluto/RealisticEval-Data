#include <iostream>
#include <regex>
#include <string>
#include <catch2/catch_test_macros.hpp>

// Test class using Catch2
TEST_CASE("TestContainsEmail", "[email]") {
    SECTION("test_contains_valid_email") {
        // Test if a valid email is detected in the string
        std::string test_string = "You can reach me at example@example.com for more info.";
        REQUIRE(contains_email(test_string));
    }

    SECTION("test_contains_email_with_special_characters") {
        // Test if an email with special characters is detected
        std::string test_string = "My email address is john.doe123+test@gmail.com!";
        REQUIRE(contains_email(test_string));
    }

    SECTION("test_does_not_contain_email") {
        // Test a string that does not contain any email address
        std::string test_string = "This string does not have an email.";
        REQUIRE_FALSE(contains_email(test_string));
    }

    SECTION("test_contains_multiple_emails") {
        // Test a string containing multiple email addresses
        std::string test_string = "You can contact me at example1@example.com or example2@example.com.";
        REQUIRE(contains_email(test_string));
    }

    SECTION("test_contains_invalid_email_format") {
        // Test a string with an invalid email format
        std::string test_string = "Please contact me at example@.com or test@domain.";
        REQUIRE_FALSE(contains_email(test_string));
    }
}