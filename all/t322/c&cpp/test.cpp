TEST_CASE("isValidEmail") {
    SECTION("should return true for a valid simple email") {
        REQUIRE(isValidEmail("test@example.com") == true); // 'test@example.com' is a valid email
    }

    SECTION("should return true for a valid email with subdomain") {
        REQUIRE(isValidEmail("user@mail.example.com") == true); // 'user@mail.example.com' is a valid email
    }

    SECTION("should return false for an email missing the @ symbol") {
        REQUIRE(isValidEmail("invalid-email.com") == false); // 'invalid-email.com' is missing the @ symbol
    }

    SECTION("should return false for an email missing the domain part") {
        REQUIRE(isValidEmail("user@.com") == false); // 'user@.com' is missing a valid domain name
    }

    SECTION("should return false for an email with spaces") {
        REQUIRE(isValidEmail("user name@example.com") == false); // 'user name@example.com' contains spaces
    }
}