#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Include or define the replacePhoneNumbers function here
std::string replacePhoneNumbers(const std::string &text) {
    std::regex phonePattern(R"(\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b)");
    std::string replacedText = std::regex_replace(text, phonePattern, "[PHONE_NUM]");
    return replacedText;
}

TEST_CASE("Basic number replacement", "[replacePhoneNumbers]") {
    std::string msg = "Call me at 123-456-7890.";
    std::string expected = "Call me at [PHONE_NUM].";
    REQUIRE(replacePhoneNumbers(msg) == expected);
}

TEST_CASE("International number replacement", "[replacePhoneNumbers]") {
    std::string msg = "Contact us at 44 123 456 789.";
    std::string expected = "Contact us at [PHONE_NUM].";
    REQUIRE(replacePhoneNumbers(msg) == expected);
}

TEST_CASE("Number with parentheses", "[replacePhoneNumbers]") {
    std::string msg = "Our office number is 123 456-7890.";
    std::string expected = "Our office number is [PHONE_NUM].";
    REQUIRE(replacePhoneNumbers(msg) == expected);
}

TEST_CASE("Number with dots", "[replacePhoneNumbers]") {
    std::string msg = "Fax us at 123.456.7890.";
    std::string expected = "Fax us at [PHONE_NUM].";
    REQUIRE(replacePhoneNumbers(msg) == expected);
}

TEST_CASE("No phone number", "[replacePhoneNumbers]") {
    std::string msg = "Hello, please reply to this email.";
    std::string expected = "Hello, please reply to this email.";
    REQUIRE(replacePhoneNumbers(msg) == expected);
}