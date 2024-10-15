TEST_CASE("isValidUsername", "[username]") {
    SECTION("should return true for a valid username with letters, numbers, and underscores") {
        REQUIRE(isValidUsername("user_123") == true); // 'user_123' is a valid username
    }

    SECTION("should return true for a valid username with only letters") {
        REQUIRE(isValidUsername("username") == true); // 'username' is a valid username
    }

    SECTION("should return false for a username with special characters") {
        REQUIRE(isValidUsername("user-name") == false); // 'user-name' contains a hyphen
    }

    SECTION("should return false for a username with spaces") {
        REQUIRE(isValidUsername("user name") == false); // 'user name' contains spaces
    }

    SECTION("should return true for a valid username with only numbers") {
        REQUIRE(isValidUsername("12345") == true); // '12345' is a valid username
    }
}