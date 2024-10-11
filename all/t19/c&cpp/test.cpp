TEST_CASE("Phone number detection tests") {
    SECTION("Test with international prefix") {
        REQUIRE(contains_phone_number("+1-800-555-1234"));
    }

    SECTION("Test with standard dashes") {
        REQUIRE(contains_phone_number("800-555-1234"));
    }

    SECTION("Test with spaces") {
        REQUIRE(contains_phone_number("800 555 1234"));
    }

    SECTION("Test without phone number") {
        REQUIRE_FALSE(contains_phone_number("Hello, world!"));
    }

    SECTION("Test with text containing numbers") {
        REQUIRE(contains_phone_number("Call me at 800-555-1234 today!"));
    }
}