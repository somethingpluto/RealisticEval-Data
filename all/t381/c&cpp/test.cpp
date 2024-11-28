TEST_CASE("TestExtractEmailDetails", "[email]") {
    SECTION("test_valid_email") {
        // Test with a typical email address
        std::string email = "user@example.com";
        std::pair<std::string, std::string> expected = {"user", "example.com"};
        auto result = extract_email_details(email);
        REQUIRE(result == expected);
    }

    SECTION("test_valid_email_with_subdomain") {
        // Test with an email that includes a subdomain
        std::string email = "user@mail.office.com";
        std::pair<std::string, std::string> expected = {"user", "mail.office.com"};
        auto result = extract_email_details(email);
        REQUIRE(result == expected);
    }

    SECTION("test_email_without_at_symbol") {
        // Test with an email that lacks an '@' symbol
        std::string email = "userexample.com";
        REQUIRE_THROWS_AS(extract_email_details(email), std::invalid_argument);
    }

    SECTION("test_empty_email") {
        // Test with an empty string as an email
        std::string email = "";
        REQUIRE_THROWS_AS(extract_email_details(email), std::invalid_argument);
    }
}