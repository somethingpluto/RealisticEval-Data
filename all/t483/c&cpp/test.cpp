TEST_CASE("Test Email Validation", "[email]") {
    SECTION("Valid email") {
        REQUIRE(is_valid_email("test@example.com"));
    }

    SECTION("Valid email with subdomain") {
        REQUIRE(is_valid_email("user@subdomain.example.com"));
    }

    SECTION("Valid email with plus tag") {
        REQUIRE(is_valid_email("user.name+tag+sorting@example.com"));
    }

    SECTION("Invalid email missing username") {
        REQUIRE_FALSE(is_valid_email("@missingusername.com"));
    }

    SECTION("Invalid email missing at symbol") {
        REQUIRE_FALSE(is_valid_email("missingatsign.com"));
    }

    SECTION("Invalid email TLD too short") {
        REQUIRE_FALSE(is_valid_email("user@domain.c"));
    }

    SECTION("Invalid email with special characters") {
        REQUIRE_FALSE(is_valid_email("user@domain.com!"));
    }
}