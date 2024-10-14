TEST_CASE("isValidUsername") {
    SECTION("valid username with alphanumeric characters") {
        REQUIRE(isValidUsername("User123") == true);
    }

    SECTION("valid username with spaces") {
        REQUIRE(isValidUsername("User 123") == true);
    }

    SECTION("invalid username that is too short") {
        REQUIRE(isValidUsername("User") == false);
    }

    SECTION("invalid username that is too long") {
        REQUIRE(isValidUsername("ThisIsAVeryLongUsername") == false);
    }

    SECTION("invalid username with special characters") {
        REQUIRE(isValidUsername("User!") == false);
    }

    SECTION("invalid username with only spaces") {
        REQUIRE(isValidUsername("     ") == false);
    }

    SECTION("invalid input type (number)") {
        // C++ does not allow passing an int to a string parameter directly.
        // Assuming isValidUsername has a proper overload or handles this internally.
        REQUIRE(isValidUsername(std::to_string(12345)) == false);
    }
}