TEST_CASE("Test PhoneNumber Detection", "[PhoneNumberDetection]") {
    SECTION("with international prefix") {
        REQUIRE(contains_phone_number("+1-800-555-1234"));
    }

    SECTION("with standard dashes") {
        REQUIRE(contains_phone_number("800-555-1234"));
    }

    SECTION("with spaces") {
        REQUIRE(contains_phone_number("800 555 1234"));
    }

    SECTION("without phone number") {
        REQUIRE_FALSE(contains_phone_number("Hello, world!"));
    }

    SECTION("with text containing numbers") {
        REQUIRE(contains_phone_number("Call me at 800-555-1234 today!"));
    }
}