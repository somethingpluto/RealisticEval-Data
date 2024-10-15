TEST_CASE("Password Validator Tests") {
    SECTION("Valid password") {
        REQUIRE(isValidPassword("Password1!") == true);
    }

    SECTION("Password without a number") {
        REQUIRE(isValidPassword("Password!") == false);
    }

    SECTION("Password without an uppercase letter") {
        REQUIRE(isValidPassword("password1!") == false);
    }

    SECTION("Password without a lowercase letter") {
        REQUIRE(isValidPassword("PASSWORD1!") == false);
    }

    SECTION("Password without a punctuation mark") {
        REQUIRE(isValidPassword("Password1") == false);
    }

    SECTION("Password shorter than 8 characters") {
        REQUIRE(isValidPassword("Pass1!") == false);
    }
}